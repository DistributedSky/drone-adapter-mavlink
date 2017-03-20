#!/usr/bin/env python
import httplib, rospy, json, os
from mavros_msgs.msg import Waypoint
from mavros_msgs.srv import WaypointPush

def get_mission():
    conn = httplib.HTTPSConnection(os.environ['IPFS_HOST'])
    conn.request('GET', '/ipfs/{0}'.format(os.environ['MISSION_HASH']))
    mission_data = conn.getresponse().read()
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
        w.x_alt  = item['coordinate'][2]
        yield w

if __name__ == '__main__':
    rospy.init_node('mission_loader', anonymous=True)
    rospy.wait_for_service('mavros/mission/push')
    push = rospy.ServiceProxy('mavros/mission/push', WaypointPush)
    push(WaypointPush(get_mission())) 
