#!/usr/bin/env python
# license removed for brevity

import rospy, random
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import *

sky_width = 10000

def manager():
    rospy.init_node('cloud_manager',anonymous=True)
    rospy.wait_for_service('gazebo/spawn_sdf_model')
    with open("/home/pedro/camera_ws/src/camera_simulation/models/my_cloud/model.sdf", "r") as f:
        model_xml = f.read()
    
    for i in range(100):
        model_name = "cloud"+str(i)
        model_pose = Pose()
        model_pose.position.z = 2000
        model_pose.position.x = random.random()*sky_width*2 -10000
        model_pose.position.y = random.random()*sky_width*2 -10000

        spawn_model = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        spawn_model(model_name, model_xml, "", model_pose, "world")
    
    

if __name__ == '__main__':
    try:
        manager()
    except rospy.ROSInterruptException:
        pass