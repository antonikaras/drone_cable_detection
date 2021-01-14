# Intelligent Collaborative DroneSystem for Cable Detection

## Description

This package was created for the course SYSTEM DESIGN OF INTELLIGENT COLLABORATING SYSTEMS at the University of Southern Denmark. The goal is to use a drone swarm in a master-slave configuration in order to inspect with a high power cable, however the requiremnt for this project is to align the two UAVs with the cable. The code developed was based on the code provided by Oscar Bowen Schofield, https://github.com/OBSchofieldUK/RM-ICS20/ . 

A video demonstation of the system is here : https://youtu.be/MYW7WCP0Eoc

The branch docker_env contains a docker environment, without the neeed to install ROS in your system, with instructions on how to run it. 

## Dependencies

* px4 firmware v1.8.2, git clone https://github.com/px4/firmware
* QGroundControl, http://qgroundcontrol.com/

## How to install

* Clone the package your using ```git clone -b docker_env https://github.com/antonikaras/drone_cable_detection.git```

### Install docker

* Docker without Nvidia graphics card https://docs.docker.com/engine/install/ubuntu/
* Docker with Nvidia graphics card https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker
* It can be benificial to add your user to the docker group such that sudo is not needed to run docker commands.
``` 
    sudo groupadd docker
    sudo usermod -aG docker $USER
    and reboot the computer
```

* Build the Docker image in the root directory of this git repo:
    
    ```docker build --tag drone_cable_detector .```

### Install the PX4 Firmware

* Download the PX4 firmware repo version and select version v1.8.2.
```    
    cd docker-workspace
    git clone https://github.com/PX4/Firmware.git
    cd Firmware
    git checkout tags/v1.8.2
    git submodule update --init --recursive
```

* And run the docker image with:
	./run-docker-image.sh or ./run-docker-image-gpu.sh

* Now build the PX4 firmware inside the Docker image according to the guide.
```
    ./run-docker-image.sh or ./run-docker-image-gpu.sh
    cd /workspace/Firmware
    make posix_sitl_default gazebo    
```

## How to use

* Terminal 1:
```
    ./run-docker-image.sh or ./run-docker-image-gpu.sh
    build-ws
    roslaunch drone_cable_detection miniproject_swarm.launch
```
* Terminal 2
```
    docker exec -it drone_cable_detector-tester bash
    src
    rosrun drone_cable_detection swarm_commander.py
```
* Terminal 3
    run QGroundControl, it is used to visualize the UAVs, create missions, etc...

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
