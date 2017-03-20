#!/bin/sh

. /tmp/build/setup.sh
export ROS_MASTER_URI="http://${MASTER:-localhost}:11311"
export HOSTNAME=$(cat /etc/hostname)
exec roslaunch drone_adapter_mavlink solo.launch
