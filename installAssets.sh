#!/bin/bash

FIRMDIR=$1
CWD=$PWD
if [[ "$FIRMDIR" == "" ]]; then
  echo "You did not supply the Firmware folder."
  exit
fi

cd $FIRMDIR

echo "installing launch files."
cp $CWD/launchFiles/* launch/ -v

echo "installing Gazebo Models."
cp -r $CWD/models/* Tools/sitl_gazebo/models/ -v

echo "installing worlds."
cp $CWD/worlds/* Tools/sitl_gazebo/worlds/ -v

#echo "installing startup scripts."
#cp $CWD/startupScripts/* . -v
