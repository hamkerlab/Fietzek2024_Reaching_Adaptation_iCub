#!/bin/bash

# starts the yarpserver and the gazebo simulator with the iCub inside

if [ $# == 0 ]
then
    file="./icub_image_scene_cam_visuomanip"

else
    file=$1
fi

screen -S iCub -dm bash -c 'screen; exec sh' # start screen with two windows

#### start yarpserver
echo "run yarpserver"
screen -S iCub -p 0 -X stuff "yarpserver --write^M"
echo "started yarpserver"
 
sleep 1

#### start iCub simulator
echo "run gazebo simulator"
screen -S iCub -p 1 -X stuff "gzserver $file.world --verbose^M"
echo "started gazebo simulator"

