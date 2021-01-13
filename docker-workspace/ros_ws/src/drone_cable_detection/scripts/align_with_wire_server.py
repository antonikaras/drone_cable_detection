#!/usr/bin/env python2

import rospy
import mavros
from sensor_msgs.msg import LaserScan as LS
from mavros import setpoint as SP
import mavros.setpoint
import mavros.command
import numpy as np
from math import atan2, atan
from std_msgs.msg import Float32, Float64, Bool
from geometry_msgs.msg import Vector3, TwistStamped
from drone_cable_detection.srv import align_with_wire, align_with_wireResponse 
import signal
import mavros_msgs.msg
import mavros_msgs.srv
import sys
import tf
from math import cos, sin
from simple_pid import PID

class AlignMasterWire():
    """
        This class acts as a server for the align_master_wire service
        @ID is the number of the master drone equiped with the VU8 LiDARs
    """
    def __init__(self, ID=1):
        
        # Generate the drone ID
        self.ID = "uav" + str(ID)
        self.nodeID = "/" + self.ID

        # Setup the node
        rospy.init_node("align_with_wire_server")

        self.rate = rospy.Rate(20)
        mavros.set_namespace(self.ID + '/mavros')

        self.current_pose = Vector3()
        self.UAV_state = mavros_msgs.msg.State()

        # Initaialize variables
        self.vu8_48_data = [0.0] * 80
        self.vu8_100_data = [0.0] * 80
        self.vu8_48_specs = [0.0] * 3
        self.vu8_100_specs = [0.0] * 3
        self.local_pos = [0.0] * 4
        self.yaw_speed = 0.0
        self.dist_speed = 0.0

        # Create threshold function
        self.chop = lambda x, thr : np.sign(x) * np.minimum(thr, abs(x)) 

        # Define the lidar subscribers
        vu8_100_lid = rospy.Subscriber("/LiDAR/VU8_100Deg/scan_raw", LS, self.vu8_100_callback)
        vu8_48_lid = rospy.Subscriber("/LiDAR/VU8_48Deg/scan_raw", LS, self.vu8_48_callback)
      
        # /mavros/local_position/pose
        local_position_sub = rospy.Subscriber(mavros.get_topic('local_position', 'pose'),
             SP.PoseStamped, self._local_position_callback)
        # /mavros/state
        state_sub = rospy.Subscriber(mavros.get_topic('state'),
                                 mavros_msgs.msg.State, self._state_callback)
        # Setup publishers
        # /mavros/setpoint_velocity/cmd_vel
        self.cmd_vel_pub = rospy.Publisher(self.ID + "/mavros/setpoint_velocity/cmd_vel", TwistStamped, queue_size=10)
        
        # setup services
        # /mavros/cmd/arming
        self.set_arming = rospy.ServiceProxy(self.nodeID + '/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        # /mavros/set_mode
        self.set_mode = rospy.ServiceProxy(self.nodeID + '/mavros/set_mode', mavros_msgs.srv.SetMode)      
        # align_with_wire_service
        al_2_wr = rospy.Service(self.ID + "/align_with_wire", align_with_wire, self.AlignUAV2Wire)
        self.setpoint_msg = mavros.setpoint.PoseStamped(
            header=mavros.setpoint.Header(
                frame_id="att_pose",
                stamp=rospy.Time.now()),
        )

        '''
        # PID subscribers
        # Define the PID publishers
        self.yaw_state_pub = rospy.Publisher("/yaw_angle/state", Float64, queue_size=10)
        self.yaw_setpoint_pub = rospy.Publisher("/setpoint_yaw", Float64, queue_size=10)

        self.dist_state_pub = rospy.Publisher("/dist/state", Float64, queue_size=10)
        self.dist_setpoint_pub = rospy.Publisher("/setpoint_dist", Float64, queue_size=10)
        
        # Define the PID subscribers
        yaw_pid_sub = rospy.Subscriber("/yaw_angle/control_effort", Float64, self.yaw_pid_callback)
        dist_pid_sub = rospy.Subscriber("/dist/control_effort", Float64, self.dist_pid_callback)

        self.yaw_speed = 0.0
        self.dist_speed = 0.0

        '''

        # Ensure that the server is running
        rospy.spin()
        
    def yaw_pid_callback(self, data):
        self.yaw_speed = data.data

    def dist_pid_callback(self, data):
        self.dist_speed = data.data

    def _state_callback(self, topic):
        self.UAV_state.armed = topic.armed
        self.UAV_state.connected = topic.connected
        self.UAV_state.mode = topic.mode
        self.UAV_state.guided = topic.guided

    def vu8_100_callback(self, data):
        
        self.vu8_100_data = data.ranges
        self.vu8_100_specs = [data.angle_min, data.angle_max, data.angle_increment]
    
    def vu8_48_callback(self, data):
        
        self.vu8_48_data = data.ranges
        self.vu8_48_specs = [data.angle_min, data.angle_max, data.angle_increment]
     
    def _local_position_callback(self, topic):
        # Position data
        self.local_pos[0] = topic.pose.position.x
        self.local_pos[1] = topic.pose.position.y
        self.local_pos[2] = topic.pose.position.z

         # Orientation data
        (r, p, y) = tf.transformations.euler_from_quaternion([topic.pose.orientation.x, topic.pose.orientation.y, topic.pose.orientation.z, topic.pose.orientation.w])
        self.local_pos[3] = y
   
    def DistWireBack(self):
        """
            Use the rear LiDAR to compute the distance and yaw angle to the wire
        """
        
        cnt = 0
        dist = 0.0
        height = 0.0
        yaw_angle = 0.0
        cnt_good = 0
        
        # ensure that the sensor has a usable value
        while (cnt < 3):
            
            # Check if the Lidar sensor got a usable mesurement
            if (min(self.vu8_100_data) != float('inf')):
                # Find the angle of the wire
                ang_index = np.argmin(self.vu8_100_data)
                ang = self.vu8_100_specs[2] * ang_index + self.vu8_100_specs[0]

                # Find the distance from the wire to the vertical axis
                dist += np.sin(ang) * self.vu8_100_data[ang_index]
                height += np.cos(ang)* self.vu8_100_data[ang_index]
                cnt_good += 1

            cnt += 1
            self.rate.sleep()

        if  cnt_good > 1:
            dist = dist / cnt_good
            height /= cnt_good
            yaw_angle = atan(dist / (-0.1))
        else :
            yaw_angle = float('inf')
            dist = float('inf')

        return dist, height, yaw_angle
    
    def DistWireFront(self):
        """
            Use the front LiDAR to compute the distance and yaw angle to the wire
        """
        cnt = 0
        dist = 0.0
        height = 0.0
        yaw_angle = 0.0
        cnt_good = 0
        
        # ensure that the sensor has a usable value
        while (cnt < 3):

             # Check if the Lidar sensor got a usable mesurement
            if (min(self.vu8_48_data) != float('inf')):
                # Find the angle of the wire
                ang_index = np.argmin(self.vu8_48_data)
                ang = self.vu8_48_specs[2] * ang_index + self.vu8_48_specs[0]

                # Find the distance from the wire to the vertical axis
                dist += np.sin(ang) * self.vu8_48_data[ang_index]
                height += np.cos(ang)* self.vu8_48_data[ang_index]

                cnt_good += 1
            
            cnt += 1
            self.rate.sleep()

        if  cnt_good > 1:
            dist = dist / cnt_good
            height /= cnt_good
            yaw_angle = atan(dist / 0.1)
        else :
            yaw_angle = float('inf')
            dist = float('inf')

        return dist, height, yaw_angle
    
    def AlignWithWire(self, timeout):
        """
            Use the LiDARs to ensure that both the front and back LiDAR detect the wire
            and then align with it in two steps, step 1 : yaw alignment, step 2 : y axis alignment
            returns 1 -> wire between the LiDARS, 0 -> wire not found
        """
        cnt = 0
        new_sp = TwistStamped()
        while self.UAV_state.mode != "OFFBOARD" :
            rospy.sleep(0.1)
            self.set_mode(0, 'OFFBOARD')
            # Publish something to activate the offboard mode
            self.cmd_vel_pub.publish(new_sp)

        mavros.command.arming(True)

        # Initialize the PID controllers
        distPID = PID(3.2, 0.56, 0.04, output_limits=(-2.0, 2.0), setpoint=0.0)
        yawPID = PID(0.32, 0.01, 0.00, output_limits=(-0.5, 0.5), setpoint=0.0)

        # Introduce a dummy movement until the OFFBOARD mode is fully activated
        ts = rospy.Time.now()
        while (rospy.Time.now() - ts < rospy.Duration(1.0)):
            self.cmd_vel_pub.publish(new_sp)
        
        last_request = rospy.Time.now()
        t0 = last_request

        aligned_cnt = 0
        
        Wire_pos = mavros_msgs.msg.PositionTarget()
        ts = rospy.Time.now()
        ts2 = rospy.Time.now()
        while ((rospy.Time.now() - ts2 < rospy.Duration(5.0)) and (aligned_cnt < 2) and (rospy.Time.now() - ts < rospy.Duration(timeout))):
            
            if (self.UAV_state.mode != "OFFBOARD" and
                    (rospy.Time.now() - last_request > rospy.Duration(5.0))):
                self.set_mode(0, 'OFFBOARD')
                print("enabling offboard mode")
                last_request = rospy.Time.now()
            else:
                if (not self.set_mode(0, 'OFFBOARD') and
                        (rospy.Time.now() - last_request > rospy.Duration(5.0))):
                    if (mavros.command.arming(True)):
                        print("Vehicle armed")
                    last_request = rospy.Time.now()
            
            dist_f, height_f, yaw_angle_f = self.DistWireFront()
            dist_b, height_b, yaw_angle_b = self.DistWireBack()
            height = 0.5 * (height_b + height_f)
            dist = 0.5 * (-(dist_b) + (dist_f))
            if (np.sign(yaw_angle_f) == np.sign(yaw_angle_b)):
                yaw_angle = (yaw_angle_f - yaw_angle_b)
            else:
                yaw_angle = (yaw_angle_f + yaw_angle_b)
            
            yaw_dist = 0.5 * (abs(yaw_angle_f) + abs(yaw_angle_b))

            # Check if the wire is already visible from both lidars
            if ((abs(dist_f) != float('inf')) and (abs(dist_b) != float('inf'))):
                #rospy.loginfo("both LiDARs" + str(0.5 * (-(dist_b) + (dist_f))) + " " +  str(yaw_dist) + " " + str(yaw_angle))
                
                ts2 = rospy.Time.now()
                new_sp = TwistStamped()
                new_sp.twist.linear.y = -distPID(dist)
                new_sp.twist.angular.z = yawPID(-yaw_angle)

                '''
                new_sp.twist.linear.y = -self.dist_speed
                new_sp.twist.angular.z = self.yaw_speed
                # Publish the states
                self.yaw_state_pub.publish(-yaw_angle)
                self.yaw_setpoint_pub.publish(0.0)
                #self.uav.NewSpeed(error)
                self.dist_state_pub.publish(dist)
                self.dist_setpoint_pub.publish(0.0)
                '''
                self.cmd_vel_pub.publish(new_sp)
            
            if ((abs(dist) < 0.1) and (abs(yaw_dist) < 0.1)):
                aligned_cnt += 1
                Wire_pos.position.x = self.local_pos[0]
                Wire_pos.position.y = self.local_pos[1]
                Wire_pos.position.z = self.local_pos[2]
                Wire_pos.yaw = self.local_pos[3]
            else:
                aligned_cnt = 0
        print(rospy.Time.now() - ts, rospy.Time.now() - ts2, cnt, aligned_cnt)

        return Wire_pos
    
    def AlignUAV2Wire(self, req):
        """
            Enter the coordinates of the wire, x, y, z, yaw
        """
        
        rospy.loginfo("Received wire coordinates")
        Wire_pos = mavros_msgs.msg.PositionTarget()
        # Go to the wire first
        try:
            #rospy.loginfo(self.ID + " has reached the wire, distance " + str(dist))

            # Align with the wire
            Wire_pos = self.AlignWithWire(req.timeOut)

        except rospy.ServiceException as exc:
                print("Service did not process request: " + str(exc))
                print("Service buisy")

        return align_with_wireResponse(Wire_pos)
    

###################################################################################################
if __name__ == "__main__":
    AMW = AlignMasterWire(1)
        