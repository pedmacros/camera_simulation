# CAMERA SIMULATION
This ROS package contains de necessary files to simulate the cloud-detector project in Gazebo.

## Requirements
- PC with Ubuntu 18.04
- ROS Melodic
- Gazebo (Custom built, see details below)
- Nvidia driver (Recommended)
- Git

## Download and Build Gazebo
To get this simulation working properly, it is necesary to use a modified version of the Gazebo simulation. Once ROS is installed, remove Gazebo if it was installed previously:

```
sudo apt-get remove '.*gazebo.*' '.*sdformat.*' '.*ignition-math.*' '.*ignition-msgs.*' '.*ignition-transport.*' 
```
### Install dependencies

1. Setup your computer to accept software from packages.osrfoundation.org:
    ```
    sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
    ```
2. Setup keys and update:
    ```
    wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
    sudo apt-get update
    ```
3. Install prerequisites. A clean Ubuntu system will need the following (replace version with the major version of gazebo you intend to build, eg: 7, 8, 9. And if using ROS, replace dummy with your ROS version, eg: indigo, jade, kinetic...):
    ```
    wget https://raw.githubusercontent.com/ignition-tooling/release-tools/master/jenkins-scripts/lib/dependencies_archive.sh -O /tmp/dependencies.sh
    GAZEBO_MAJOR_VERSION=version ROS_DISTRO=dummy . /tmp/dependencies.sh
    echo $BASE_DEPENDENCIES $GAZEBO_BASE_DEPENDENCIES | tr -d '\\' | xargs sudo apt-get -y install
    ```
### Download, modify and install Gazebo

1. Clone the repository into a directory and go into it:
   
    ```
    git clone https://github.com/osrf/gazebo /tmp/gazebo
    ```

2. Navigate to the folder containing the file WideAngleCameraSensor.cc:
   
    ```
    cd /tmp/gazebo/gazebo/sensors
    ```

3. Open WideAngleCameraSensor.cc with a text editor, look for this code and comment it:
   
    ```
    // Disable clouds and moon on server side until fixed and also to improve
    // performance
    this->scene->SetSkyXMode(rendering::Scene::GZ_SKYX_ALL &
        ~rendering::Scene::GZ_SKYX_CLOUDS &
        ~rendering::Scene::GZ_SKYX_MOON);
    ```
4. Create a build directory and go there:
   
    ```
    cd /tmp/gazebo
    mkdir build
    cd build
    ```

5. Configure Gazebo:
    ```
    cmake ../
    ```

6. The output from cmake ../ may generate a number of errors and warnings about missing packages. You must install the missing packages that have errors and re-run cmake ../. Make sure all the build errors are resolved before continuing (they should be there from the earlier step in which you installed prerequisites). Warnings alert of optional packages that are missing.
   
7. Make note of your install path, which is output from cmake and will either be the default install location or the one specified as <install_path> above, e.g.:
    ```
    -- Install path: /home/$USER/local
    ```

8. Build Gazebo:

    ```
    make -j4
    ```

9. Install Gazebo:
    
    ```
    sudo make install
    ```

Now you can try running Gazebo:

```
gazebo
```

## Launch simulation
Once the workspace has been compiled and source, the simulation can be run:

```
roslaunch camera_simulation camera_world.launch
```

## References
- <https://answers.gazebosim.org//question/20177/clouds-from-screen-is-not-visible-in-camera-image/>
- <http://gazebosim.org/tutorials?tut=install_from_source&cat=install#ROSUsers>