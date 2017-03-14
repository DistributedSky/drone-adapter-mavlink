#!/bin/sh

. /opt/ros/kinetic/setup.sh
export ROS_MASTER_URI="http://${MASTER:-localhost}:11311"
export HOSTNAME=$(cat /etc/hostname)
exec roslaunch /mavros.launch
