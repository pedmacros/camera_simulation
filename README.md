# CAMERA SIMULATION
This ROS package contains de necessary files to simulate the cloud-detector project in Gazebo.

Currently, the simulation consist of two fisheye cameras pointing to the sky and one static cloud.

## Requirements
- PC with Ubuntu 18.04
- ROS Melodic
- Gazebo
- Nvidia driver (Recommended)
- Git


## Launch simulation
Once the workspace has been compiled and sourced, the simulation can be run:

```
roslaunch camera_simulation camera_world.launch
```

## cloud_manager node
The cloude_manager node is meant to allow real time customization of the clouds in the simulation, allowing the user to tune their movement speed and the amount of clouds spawned. Once the simulation has been launched, the cloud manager node can be run as follows:

``` 
rosrun camera_simulation cloud_manager.py
```
### spawn_clouds

This node provides two different services. The first one, spawn_clouds, can be use to create new clouds in the simulation. It takes as parameters the number of desired clouds and their speed vectors in X and Y axis. The clouds are spawned randomly across a 10 x 10 km square and at different height ranging between 1000 and 1500 m. For example, the service can be requested as follows:

```
rosservice call spawn_clouds "count: 15
vx: 10.0
vy: 20.0"
```

This service can be called multiple times, with differente parameters each time.

### remove_clouds

This service remove all clouds that have been spawn previously. It may take a few minutes to remove all the clouds if a big amount of them has been spawned previously.

```
rosservice call /remove_clouds "{}"
```

## Sun position script

Inside the scripts folder there is a test.py that can be use to test the prediction of the sun in the sky relative to a point in the surface of Earth. Latitud, longitud and time data can be changed to obtain the diferent azimuth and elevation angles.

To test it, modify the values in the script and run it:

```
python test_sun_pos.py
```

## References
- <https://answers.gazebosim.org//question/20177/clouds-from-screen-is-not-visible-in-camera-image/>
- <http://gazebosim.org/tutorials?tut=install_from_source&cat=install#ROSUsers>