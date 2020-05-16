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
from collab_agents_miniproject.srv import align_with_wire, align_with_wireResponse 
import sys
import signal
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32
import math
import numpy as np
import utm
from simpleDrone import SimpleDrone as SD
from allign_with_wire_v2 import AlignUAV as AUAV

class SwarmCommander():
    """
        Class that sends the instructions to the two drones
    """

    def __init__(self):
        
        # Initialize the new node
        rospy.init_node("swarm_commander")
        self.rate = rospy.Rate(20)

        # Attach the two drones
        self.uav1 = SD(1)
        self.uav2 = SD(2, UAVtype="slave")

        # Initialize the wire position
        self.wire_pos = [-45.0, 15, 10.0, 1.5]

        # Initialize align with wire server        
        self.align_with_wire_serv = rospy.ServiceProxy("uav1/align_with_wire", align_with_wire)

        # Initialize the distance between the master and slave uav
        self.uavDist = [1, 0, 0, 0]

        self.InputHandler()

    def ComputeNewPosition(self, pos = None):
        """ If the swarm effect is activated then uav2 will follow uav1"""
        newPos = np.zeros((1, 4))
        if pos:
            newPos[0] = pos.position.x 
            newPos[1] = pos.position.y 
            newPos[2] = pos.position.z 
            newPos[3] = pos.yaw
        else:
            newPos = np.array(self.uav1.local_pos)

        newPos -= np.array(self.uavDist)
        newPos[0] += 2 * np.cos(self.uav1.local_pos[3])
        newPos[1] += 2 * np.sin(self.uav1.local_pos[3])
        
        return newPos

    def Help(self):
        """ Print the instructions the swarm commander recognizes"""
        print("----- Swarm commander available inputs -----")
        print("exit -> to close the swarm commander")
        print("uav#  corresponds to either uav1 or uav2")
        print("uav# goto x y z yaw  -> uav# will go to the  specified location location")
        print("uav# land [x y z yaw] -> uav# will land at its current position or at the optional x, y, z, yaw")
        print("uav# return -> uav# will return to its home position and land")
        print("uav1 distance uav2 x y z yaw -> assign the distance from uav1 to uav2")
        print("uav2 distance uav1 x y z yaw -> assign the distance from uav2 to uav1")
        print("uav# align [timeOut] -> uav# will try to align with the wire at its current position, timeOut is optional")
        print("--------------------------------------------")
    
    def InputHandler(self):
        """ Used to handle the keyboard inputs from the terminal"""
        done = False
        WirePos = mavros_msgs.msg.PositionTarget()
        swarmEffect = False
        while not done:
            inp = raw_input("Type your command > ")
            inp = inp.split()
            print(len(inp), (inp))
            
            if len(inp) == 1:
                if inp[0] == 'exit':
                    done = True
                else:
                    self.Help()
            elif len(inp) > 1:
                pos = []
                uavID = inp[0]
                if (len(inp) == 6):
                    pos.append(float(inp[2]))
                    pos.append(float(inp[3]))
                    pos.append(float(inp[4]))
                    pos.append(float(inp[5]))

                if inp[1] == 'goto':
                    if len(inp) != 6 and len(inp) != 3:
                        self.Help()
                        continue
                    if uavID == 'uav1':                            
                        dist = self.uav1.GotoPos(pos)
                        self.uav1.Hover()
                        if swarmEffect:
                            pos = self.ComputeNewPosition()
                            dist = self.uav2.GotoPos(pos)
                            self.uav2.Hover()
                    elif uavID == 'uav2':
                        if inp[2] == 'uav1':
                            pos = self.ComputeNewPosition()
                            dist = self.uav2.GotoPos(pos)
                        else:
                            dist = self.uav2.GotoPos(pos)
                        self.uav2.Hover()
                    else:
                        self.Help() 
                        continue
                    print("Position reached, distance ", dist) 
                elif inp[1] == 'land':
                    if uavID == 'uav1':
                        self.uav1.Land(pos)
                        if swarmEffect:
                            pos = self.ComputeNewPosition()
                            self.uav2.Land(pos)
                    elif uavID == 'uav2':
                        self.uav2.Land(pos)
                    else:
                        self.Help()
                elif inp[1] == 'return':
                    if uavID == 'uav1':
                        self.uav1.Return()
                        if swarmEffect:
                            self.uav2.Return()
                    elif uavID == 'uav2':
                        self.uav2.Return()
                    else:
                        self.Help()
                elif inp[1] == 'align':
                    timeout = 120
                    if len(inp) == 3:
                        timeout = float(inp[2])
                    if uavID == 'uav1':
                        WirePos = self.align_with_wire_serv(timeout)
                        WirePos = WirePos.wire_pos
                        self.uav1.Hover()
                        if swarmEffect:
                            pos = self.ComputeNewPosition(WirePos)
                            dist = self.uav2.GotoPos(pos)
                            self.uav2.Hover()
                    elif uavID == 'uav2':
                        pos = self.ComputeNewPosition(WirePos)
                        dist = self.uav2.GotoPos(pos)
                        self.uav2.Hover()
                    else:
                        self.Help()
                        continue
                    print(WirePos)
                elif inp[1] == 'distance':
                    if len(inp) == 7:
                        if inp[2] == 'uav1':
                            self.uavDist = [float(inp[3]), float(inp[4]), float(inp[5]), float(inp[6])]
                        elif inp[2] == 'uav2':
                            self.uavDist = [-float(inp[3]), -float(inp[4]), -float(inp[5]), -float(inp[6])]
                        else:
                            self.Help()
                    else:
                        self.Help()
                elif inp[0] == 'swarm':
                    if inp[1] == 'enable':
                        swarmEffect = True
                    elif inp[1] == 'disable':
                        swarmEffect = False
                    else:
                        self.Help()
                else:
                    self.Help()
            else:
                self.Help()


###################################################################################################
if __name__ == "__main__":
    SW = SwarmCommander()
