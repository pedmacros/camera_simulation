#!/usr/bin/env python
# license removed for brevity

import rospy, random, sys, tf
from gazebo_msgs.srv import SpawnModel, SetModelState, DeleteModel
from gazebo_msgs.msg import ModelState
from camera_simulation.srv import SpawnClouds
from geometry_msgs.msg import *
from std_srvs.srv import Empty

sky_width = 10000
clouds_count = 0

with open(sys.path[0] + '/../models/my_cloud/model.sdf', "r") as f:
    model_xml = f.read()


def spawn_clouds(req):
    global clouds_count
    spawn_model = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
    set_model = rospy.ServiceProxy('gazebo/set_model_state', SetModelState)

    for i in range(req.count):
        model_name = "cloud"+str(i+clouds_count)

        quaternion = tf.transformations.quaternion_from_euler(0, 0, (random.random()*180-90))

        model_pose = Pose()
        model_pose.position.z = random.random()*1000 + 1500
        model_pose.position.x = random.random()*sky_width*2 -10000
        model_pose.position.y = random.random()*sky_width*2 -10000
        model_pose.orientation.x = quaternion[0]
        model_pose.orientation.y = quaternion[1]
        model_pose.orientation.z = quaternion[2]
        model_pose.orientation.w = quaternion[3]

        model_state = ModelState()
        model_state.model_name = model_name
        model_state.pose = model_pose
        model_state.twist.linear.x = req.vx
        model_state.twist.linear.y = req.vy

        spawn_model(model_name, model_xml, "", model_pose, "world")
        set_model(model_state)

    clouds_count += req.count


def remove_clouds(req):
    global clouds_count
    delete_model = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
    for i in range(clouds_count):
        model_name = "cloud"+str(i)
        try:
            delete_model(model_name)
        except:
            print("Minor Error")
    clouds_count = 0




def manager():
    rospy.init_node('cloud_manager',anonymous=True)
    rospy.wait_for_service('gazebo/spawn_sdf_model')
    rospy.wait_for_service('gazebo/delete_model')

    spawner = rospy.Service('spawn_clouds', SpawnClouds, spawn_clouds)
    killer = rospy.Service('remove_clouds', Empty, remove_clouds)

    rospy.spin()


    
    

if __name__ == '__main__':
    try:
        manager()
    except rospy.ROSInterruptException:
        pass