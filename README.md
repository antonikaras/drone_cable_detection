# Intelligent Collaborative DroneSystem for Cable Detection

## Description

This package was created for the course SYSTEM DESIGN OF INTELLIGENT COLLABORATING SYSTEMS at the University of Southern Denmark. The goal is to use a drone swarm in a master-slave configuration in order to inspect with a high power cable, however the requiremnt for this project is to align the two UAVs with the cable. The code developed was based on the code provided by Oscar Bowen Schofield, https://github.com/OBSchofieldUK/RM-ICS20/ . 

A video demonstation of the system is here : https://youtu.be/MYW7WCP0Eoc

The branch docker_env contains a docker environment, without the neeed to install ROS in your system, with instructions on how to run it.

## Dependencies

* ros-melodic, or ros-kinetic,
* the mavros package v1.8.2, https://dev.px4.io/v1.8.2/en/ros/mavros_installation.html
* the mavlink ros package,
* the simple_pid python package, pip install simple-pid
* px4 firmware v1.8.2, git clone https://github.com/px4/firmware
* QGroundControl, http://qgroundcontrol.com/

## How to use

* Clone the package your catkin_workspace/src, using https://github.com/antonikaras/drone_cable_detection.git
* Execute the bash script installAssets.sh followed by the location of the px4 firmware
* Add the location of the px4 firmware to the file /sripts/px4_launch_gazebo.sh, FIRMDIR
* catkin build/ catkin_make 
* source devel/setup.bash
* roslaunch drone_cable_detection miniproject_swarm.launch
* rosrun drone_cable_detection swarm_commander.py
* run QGroundControl, required to enable the UAV to switch to hover mode

## Swarm commander command list

* exit, to close the swarm commander
* uav# goto x y z yaw, uav# will go to the  specified location location
    *  examples : ``` uav1 goto -46 15 13 1.5 ```, ``` uav2 goto uav1 ```
* uav# land [x y z yaw] -> uav# will land at its current position or at the optional x, y, z, yaw
    * examples : ``` uav1 land ```, ``` uav1 land 1 5 5 1.2 ```
* uav# return -> uav# will return to its home position and land
    * example : ``` uav2 return ```
* uav1 distance uav2 x y z yaw -> assign the distance from uav1 to uav2
* uav2 distance uav1 x y z yaw -> assign the distance from uav2 to uav1
* uav# align [timeOut] -> uav# will try to align with the wire at its current position, timeOut is optional. For the second uav to align the first one must be aligned first
    * examples : ``` uav2 align ```, ``` uav1 align 30 ```    
