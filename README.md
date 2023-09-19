# Niryo_Twin
# Contents:
- [Niryo PT and Simulation Data](#niryo-pt-and-simulation-data)
    - [1. Physical Twin:](#1-physical-twin)
        - [Method to run:](#method-to-run)
    - [2. Digital Twin (Simulation - Webots):](#2-digital-twin-simulation---webots)
        - [Requirements:](#requirements)
        - [Method to run:](#method-to-run-1)
    - [3. Digital Twin (Simulation - Gazebo):](#3-digital-twin-simulation---gazebo)
        - [Requirements:](#requirements-1)
        - [ROS Melodic Installation:](#ros-melodic-installation)
        - [Method to run:](#method-to-run-2)
- [Robot Object Detection and grasping Model:](#robot-object-detection-and-grasping-model)
    - [Docker for Niryo socks sorting:](#docker-for-niryo-socks-sorting)
- [Collaborative Robot Arm:](#collaborative-robot-arm)
    - [Requirements:](#requirements-2)
    - [Method to run:](#method-to-run-3)

# Niryo PT and Simulation Data
### 1. Physical Twin:
The required files and properties to run for physical twin are:
- Niryo Ned robot
- Scripts under `Physical_Twin_File/` folder

##### Method to run:
Sure! Here is the rephrased version of the given instructions in markdown format:

1. Before starting, make sure to have the updated firmware of the Niryo Ned robot. You can obtain the firmware from the [Niryo Studio website](https://docs.niryo.com/dev/pyniryo/v1.1.2/en/source/setup/installation.html).

2. The scenarios are defined within the `robot_movement.py` file. You can run any scenario by calling the script with the appropriate keyword arguments, ranging from (1 to 4). For example, to execute scenario 1, use the following command: `robot_movement.py 1`.

3. For logging the data, you can use the `get_logs.py` script with two keyword arguments. The first argument represents the scenario number (1 to 4), and the second argument represents the iteration number (1 to 5). To log data for scenario 1 and iteration 1, use the command: `get_logs.py 1 1`.

```py
# To run scenario 1
python robot_movement.py 1

# To record Logs:
python get_logs.py 1 1  # for scenario 1 iteration 1
```

1. This will create a log file named `scenario1_iteration1.txt` in the current folder.

2. If you want to include your own scenario just add your scenario to the `custom_robot_movement.py` file under `TODO: section`and call it with the appropriate keyword argument. eg:
```
python custom_robot_movement.py 1
```
eg:
```
# Scenario 1
scenarios = [
    # Your custom scenarios:
                [
                    [0, 0, 0, 0, 0, 0],
                    [0.096, -0.592, 0.673, -1.738, -1.499, 0.003],
                    [-1.253, -0.592, -0.079, -0.054, -0.750, 0.003],
                    [2.495, 0.610, 0.074, 1.770, -1.441, 0.003],
                    [0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
                    [0, 0, 0, 0, 0, 0]
                ],
            ]
```
1. To Add custom scenario, add the scenario to the `custom_robot_movement.py` file Under `TODO: section` and call it with the appropriate keyword argument. eg:

```
python custom_robot_movement.py 1
```


### 2. Digital Twin (Simulation - Webots):

#### Requirements:
- Webots 2023a https://github.com/cyberbotics/webots/releases/tag/R2023a
- URDF model of Niryo Ned robot
- urdf and .py under `Digital_Twin_Webots/` folder

#### Method to run:
1. Open Webots which is installed in windows or linux and load the `Niryo_Ned.wbt` under creating new wrold. Or else create new Niryo Ned robot and load the `Niryo_Ned.urdf` file which is available under `Digital_twin_Files.
2. On the right side in code section load the `webots_ned_controll.py` under `Digital_Twin_Webots`.
3. And run the `webots_ned_controll.py` file.
4. Logs will be automatically saved in current dir with name `scenario1_run_1.txt` format. (on default it will run each scenarios and 4 iterations)

5. If you want to add your own scenario just add your scenario to the `custom_webots_ned_controll.py` under `TODO: section` and run the file inside webots compiler. 


### 3. Digital Twin (Simulation - Gazebo):

#### Requirements:
- Ubuntu 18.04 
- Ros Melodic(instruction below)
- Github Repo: https://github.com/cdl-mint/ned_ros_master

#### ROS Melodic Installation:
```
### Prepare system ###
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

# Additionally thesepackages are must be installed if not there already in system:
build-essential
sqlite3
ffmpeg
"""

### Pre-installations ###
pip2 install rpi_ws281x==4.3.4
pip2 install Adafruit-GPIO==1.0.3
pip2 install Adafruit-PureIO==1.0.1
pip2 install Adafruit-BBIO==1.0.9
pip2 install Adafruit-ADS1x15==1.0.2
pip2 install board==1.0
pip2 install smbus==1.1.post2
pip2 install smbus2==0.4.1
pip2 install spidev==3.5
pip2 install gTTS==2.2.3
pip2 install psutil==5.9.0

### Creating ROS DIR and Sourcing from CDL - MINT git Repo ###
mkdir -p catkin_ws_niryo_ned/src
cd catkin_ws_niryo_ned
git clone https://github.com/cdl-mint/ned_ros_master src

### ROS Melodic Installation ###
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt install curl 

curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

sudo apt update

sudo apt install ros-melodic-desktop-full

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

source ~/.bashrc

source /opt/ros/melodic/setup.bash

sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential

sudo apt install python-rosdep

sudo rosdep init

rosdep update

### Install additional packages ### 
sudo apt install catkin
sudo apt install python-catkin-pkg
sudo apt install python-pymodbus
sudo apt install python-rosdistro
sudo apt install python-rospkg
sudo apt install python-rosdep-modules
sudo apt install python-rosinstall python rosinstall-generator 
sudo apt install python-wstool

### Install Melodic packages ###
sudo apt install ros-melodic-moveit
sudo apt install ros-melodic-control
sudo apt install ros-melodic-controllers
sudo apt install ros-melodic-tf2-web-republisher
sudo apt install ros-melodic-rosbridge-server
sudo apt install ros-melodic-joint-state-publisher-gui

### Setup Ros Env ### 
catkin_make

source devel/setup.bash

echo "source $(pwd)/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

#### Method to run:
- Run the following command to launch the simulation:
```
roslaunch niryo_robot_bringup desktop_rviz_simulation.launch
```
- open rviz by typing `rviz` in terminal eg:
```
rviz
```
- The Robot Model will be loaded in Gazebo, now we can able to control and manipulate the robot.

- To Control and get data from the robot, we `Digital_Twin_Gazebo/ned_controll.py` file. you can run the file by typing the following command in terminal:
```
python ned_controll.py 1 # for scenario 1
```
- To record the logs, simultaneously run the `get_logs.py` file. eg:
```
python get_logs.py 1 1 # 1 for diffrent iterations for scenario 1
```
- The logs will be saved in the current directory with the name `scenario1_run_1.txt` format.

# Robot Object Detection and grasping Model:
For this please refer to this seperate repository:
https://github.com/cdl-mint/Robot-Arm-for-Sorting-Mechanism-using-ROS-and-YOLOv4

Method to run: Please refer to the README.md file in the above repo.
- Requirements: Docker File from this Repo
- Place it in gpu server and create docker container from the docker file.

### Docker for Niryo socks sorting:
- This will create the xhost which allows the docker to access the host display.
```
xhost local:docker
```

- **Running the docker file:**
```py
sudo docker run -it --rm --privileged --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --device="/dev/video0:/dev/video0" cdl:socks
```

- **Running the model without entering into docker:**
```
sudo docker run -it --rm --privileged --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --device="/dev/video0:/dev/video0" cdl:socks_storing2 python3 inference/only_camera_inference.py
```
# Collaborative Robot Arm:
This part used to transfer objects from one conveyor to another conveyor. 
- The code is available in `Collaborative_Robot_Arm/` folder.

### Requirements:
- 2 Niryo Ned robots
- IP's of both the robots
- `Collaborative_Robot_Arm/` folder
- `pyniryo` lybrary installed on seperate computer

### Method to run:
1. Get a seperate computer and install `pyniryo` library. if not installed please enter this terminal command:
```
pip install pyniryo
```
2. Run the .py file in the `Collaborative_Robot_Arm/` tranfer_object_between_robots.py. eg:
```py
python transfer_object_between_robots.py
```