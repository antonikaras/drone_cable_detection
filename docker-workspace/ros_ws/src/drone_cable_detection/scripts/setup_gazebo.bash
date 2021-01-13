#!/bin/bash

export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/workspace/Firmware
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/workspace/Firmware/Tools/sitl_gazebo

source /workspace/Firmware/Tools/setup_gazebo.bash /workspace/Firmware /workspace/Firmware/build/posix_sitl_default
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/workspace/Firmware:/workspace/Firmware/Tools/sitl_gazebo

echo ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH
