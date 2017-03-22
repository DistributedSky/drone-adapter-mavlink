FROM ros:kinetic-ros-base

RUN apt-get update 
RUN apt-get install -y sudo wpasupplicant dhcpcd5
RUN easy_install web3

ADD ./drone_adapter_mavlink /tmp/build/src/drone_adapter_mavlink
RUN . /opt/ros/kinetic/setup.sh \
    && cd /tmp/build/src \
    && catkin_init_workspace \
    && cd .. \
    && rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y \
    && catkin_make

ADD ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
