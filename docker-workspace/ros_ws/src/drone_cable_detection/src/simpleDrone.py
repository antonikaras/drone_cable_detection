#!/usr/bin/env python2

# import ROS libraries
import rospy
import mavros
from mavros.utils import *
from mavros import setpoint as SP
import mavros.setpoint
import mavros.command
import mavros_msgs.msg
import mavros_msgs.srv
from sensor_msgs.msg import NavSatFix
from drone_cable_detection.srv import target_global_pos, target_global_posResponse, target_local_pos, target_local_posResponse 
import sys
import signal
from geometry_msgs.msg import Vector3, TwistStamped
from std_msgs.msg import Float32
import math
import numpy as np
import utm
import tf


class SimpleDrone():
    """
        Class that connects with a drone using mavros at the gazebo simulation
        @ID the ID number of the drone, @type= specify if the drone is a master or a slave
        @masterID, if the drone is a slave specify the master drone
    """

    def __init__(self, ID, node_name="", UAVtype="master"):
        
        # Generate the drone ID
        self.ID = "uav" + str(ID)
        self.nodeID = "/" + self.ID

        # Initialize position variables
        self.local_pos = [0.0] * 4
        self.global_pos = [0.0] * 4

        # Initialize the nodes
        if (node_name != ""):
            rospy.init_node(node_name)

        self.rate = rospy.Rate(20)
        mavros.set_namespace(self.ID + '/mavros')

        signal.signal(signal.SIGINT, self.signal_handler)

        self.current_pose = Vector3()
        self.UAV_state = mavros_msgs.msg.State()

        # setup subscribers
        # /mavros/state
        state_sub = rospy.Subscriber(mavros.get_topic('state'),
                                     mavros_msgs.msg.State, self._state_callback)

        # /mavros/local_position/pose
        local_position_sub = rospy.Subscriber(mavros.get_topic('local_position', 'pose'),
             SP.PoseStamped, self._local_position_callback)

        # /mavros/setpoint_raw/target_local
        setpoint_local_sub = rospy.Subscriber(mavros.get_topic('setpoint_raw', 'target_local'),
                                          mavros_msgs.msg.PositionTarget, self._setpoint_position_callback)
        # /mavros/global_position/global
        global_position_sub = rospy.Subscriber(self.ID + '/mavros/global_position/global',
             NavSatFix, self._global_position_callback)

        # setup publisher
        # /mavros/setpoint/position/local
        self.setpoint_local_pub = mavros.setpoint.get_pub_position_local(queue_size=10)
        # /mavros/setpoint_velocity/cmd_vel
        self.cmd_vel_pub = rospy.Publisher(self.ID + "/mavros/setpoint_velocity/cmd_vel", TwistStamped, queue_size=10)

        # setup services
        # /mavros/cmd/arming
        self.set_arming = rospy.ServiceProxy(self.nodeID + '/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        # /mavros/set_mode
        self.set_mode = rospy.ServiceProxy(self.nodeID + '/mavros/set_mode', mavros_msgs.srv.SetMode)      
        # goto_pos_services
        self.goto_glo_pos_serv = rospy.ServiceProxy(self.ID + "/target_global_pos", target_global_pos)
        self.goto_loc_pos_serv = rospy.ServiceProxy(self.ID + "/target_local_pos", target_local_pos)

        self.setpoint_msg = mavros.setpoint.PoseStamped(
            header=mavros.setpoint.Header(
                frame_id="att_pose",
                stamp=rospy.Time.now()),
        )
        
        # wait for FCU connection
        while (not self.UAV_state.connected):
            self.rate.sleep()

        rospy.loginfo("The " + self.ID + " was successfully connected")

        #rospy.spin()

    def signal_handler(self, signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

    def _state_callback(self, topic):
        self.UAV_state.armed = topic.armed
        self.UAV_state.connected = topic.connected
        self.UAV_state.mode = topic.mode
        self.UAV_state.guided = topic.guided

    def _setpoint_position_callback(self, topic):
        pass

    def _local_position_callback(self, topic):
        # Position data
        self.local_pos[0] = topic.pose.position.x
        self.local_pos[1] = topic.pose.position.y
        self.local_pos[2] = topic.pose.position.z

         # Orientation data
        (r, p, y) = tf.transformations.euler_from_quaternion([topic.pose.orientation.x, topic.pose.orientation.y, topic.pose.orientation.z, topic.pose.orientation.w])
        self.local_pos[3] = y
        self.global_pos[3] = y
        
    def _global_position_callback(self, data):
        self.global_pos[0] = data.latitude
        self.global_pos[1] = data.longitude
        self.global_pos[2] = data.altitude

    def _set_pose(self, pose, x, y, z):
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = z
        pose.header = mavros.setpoint.Header(
            frame_id="att_pose",
            stamp=rospy.Time.now())

    def update_setpoint(self):
        pass
    
    def SimpleMovement(self):
        """ Perform a circlular movement for 20 seconds """

        self.set_mode(0, 'OFFBOARD')
        mavros.command.arming(True)
        last_request = rospy.Time.now()
        t0 = last_request
        # enter the main loop
        while (rospy.Time.now() - t0 < rospy.Duration(20)):
            # print "Entered whiled loop"
            if (self.UAV_state.mode != "OFFBOARD" and
                    (rospy.Time.now() - last_request > rospy.Duration(5.0))):
                self.set_mode(0, 'OFFBOARD')
                print("enabling offboard mode")
                last_request = rospy.Time.now()
            else:
                if (not self.UAV_state.armed and
                        (rospy.Time.now() - last_request > rospy.Duration(5.0))):
                    if (mavros.command.arming(True)):
                        print("Vehicle armed")
                    last_request = rospy.Time.now()

            #setpoint_msg.pose.position.z = 3 + 2*math.sin(rospy.get_time() * 0.2)

            # Make a circle
            self.setpoint_msg.pose.position.x = 2 * math.sin(rospy.get_time() * 0.2)
            self.setpoint_msg.pose.position.y = 2 * math.cos(rospy.get_time() * 0.2)
            #print("Height: %f" % self.setpoint_msg.pose.position.z)
            self.setpoint_local_pub.publish(self.setpoint_msg)
            self.rate.sleep()

    def Hover(self):
        """
            Used to keep the altitude and position of the drone stable once activated
        """
        print("Hover", self.set_mode(0, 'AUTO.LOITER'))
    
    def GotoPos(self, pos, pos_type = "local"):
        """
            Gets the drone to the defined pos,
            @pos_type = "local" for movement on the local coordinate system, pos[4] = [x, y, z, Yaw]
            @pos_type = "global" for movement using the global coordinate system pos[4] = [Lat, Lon, Alt, Yaw]
        """

        # Deactivate the hover function if activated
        dist = -1
        if (pos_type == "local"):
            loc_pos = mavros_msgs.msg.PositionTarget(
                        header=mavros.setpoint.Header(
                            frame_id="att_pose",
                            stamp=rospy.Time.now()),
                        )
            # Position
            loc_pos.position.x = pos[0]
            loc_pos.position.y = pos[1]
            loc_pos.position.z = pos[2]

            # Orientation
            loc_pos.yaw = pos[3]

            # Call the service
            try:
                dist = self.goto_loc_pos_serv(loc_pos)
            except rospy.ServiceException as exc:
                print("Service did not process request: " + str(exc))
                print("Service buisy")
                
        if (pos_type == "global"):
            glob_pos = mavros_msgs.msg.GlobalPositionTarget(
                        header=mavros.setpoint.Header(
                            frame_id="att_pose",
                            stamp=rospy.Time.now()),
                        )
            
            # Position 
            glob_pos.latitude = pos[0]
            glob_pos.longitude = pos[1]
            glob_pos.altitude = pos[2]
            
            # Orientation
            glob_pos.yaw = pos[3]
            try:
                dist = self.goto_glo_pos_serv(glob_pos)
            except rospy.ServiceException as exc:
                print("Service did not process request: " + str(exc))
                print("Service buisy")
        
        return dist
    
    def Land(self, pos = []):
        ''' Land the UAV at its current\given position '''
        if len(pos) > 0:
            self.GotoPos(pos)
        
        self.set_mode(0, 'AUTO.LAND')
        #mavros.command.arming(False)

    def Return(self):
        ''' Return to the home pos and land'''
        self.set_mode(0, 'AUTO.RTL')
        #mavros.command.arming(False)

###################################################################################################        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: simpleDrone.py ID")

    SD = SimpleDrone(int(sys.argv[1]))
    #SD2 = SimpleDrone(2)
    #SD2.GotoLocalPos(5, 5, 10)
    #SD2.SimpleMovement()
    #SD1.GotoGlobPos(55.43600, 10.46091, 540)