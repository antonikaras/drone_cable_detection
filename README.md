# Intelligent Collaborative DroneSystem for Cable Detection

## Description

This package was created for the course SYSTEM DESIGN OF INTELLIGENT COLLABORATING SYSTEMS at the University of Southern Denmark. The goal is to use a drone swarm in a master-slave configuration in order to inspect with a high power cable, however the requiremnt for this project is to align the two UAVs with the cable. The code developed was based on the code provided by Oscar Bowen Schofield, https://github.com/OBSchofieldUK/RM-ICS20/ .

## Dependencies

* ros-melodic, or ros-kinetic,
* the mavros package v1.8.2, https://dev.px4.io/v1.8.2/en/ros/mavros_installation.html
* the mavlink ros package,
* the simple_pid python package, pip install simple-pid
* px4 firmware, git clone https://github.com/px4/firmware

## How to use

* Clone the package your catkin_workspace/src, using https://github.com/antonikaras/drone_cable_detection.git
* Execute the bash script installAssets.sh followed by the location of the px4 firmware
* Add the location of the px4 firmware to the file /sripts/px4_launch_gazebo.sh, FIRMDIR
* catkin build/ catkin_make 
* source devel/setup.bash
* roslaunch drone_cable_detection miniproject_swarm.launch
* rosrun drone_cable_detection swarm_commander.py