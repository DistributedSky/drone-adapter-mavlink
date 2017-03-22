#!/usr/bin/env python
import urllib2, rospy, json, os
from mavros_msgs.msg import Waypoint
from route_mutex import Route

def get_mission(mission_hash):
    mission_url = 'http://{0}/ipfs/{1}'.format(os.environ['IPFS_HOST'],
                                               mission_hash)
    mission_data = urllib2.urlopen(mission_url).read()
    mission_items = json.loads(mission_data)['items']
    for item in mission_items:
        w = Waypoint()
        w.frame = item['frame']
        w.command = item['command']
        w.autocontinue = item['autoContinue']
        w.param1 = item['param1']
        w.param2 = item['param2']
        w.param3 = item['param3']
        w.param4 = item['param4']
        w.x_lat  = item['coordinate'][0]
        w.y_long = item['coordinate'][1]
        w.z_alt  = item['coordinate'][2]
        yield w

if __name__ == '__main__':
    rospy.init_node('mission_loader', anonymous=True)

    rospy.wait_for_service('mavros/mission/push')
    push = rospy.ServiceProxy('mavros/mission/push', WaypointPush)

    mission = os.environ['MISSION_HASH'].strip()
    if len(mission) > 0:
        rospy.info('Try to load mission {0}'.format(mission))
        route = Route(mission)
        try:
            route.acquire()
            push(list(get_mission(mission)))
            rospy.info('Route {0} acquired and loaded'.format(mission))
        except:
            route.release()
            rospy.error('Unable to load route {0}'.format(mission))
    else:
        rospy.warn('No mission specified, skip loading')
