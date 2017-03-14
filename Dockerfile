FROM ros:kinetic-ros-base

RUN apt-get update 
RUN apt-get install -y sudo wpasupplicant dhcpcd5 ros-kinetic-mavros

ADD ./mavros.launch /mavros.launch
ADD ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
