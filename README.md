

## Installation

This will assume that you already have a catkin workspace. Go to the source directory of the workspace
  ```
  $ roscd; cd ../src
  ```
Clone this and the gripper (robotiq) repositories
  ```
  $ git clone https://github.com/ravani-org/shr
  $ git clone https://github.com/utecrobotics/robotiq
  $ git clone https://github.com/JenniferBuehler/general-message-pkgs.git
  $ git clone https://github.com/JenniferBuehler/gazebo-pkgs.git
  ```
Build using catkin_make
  ```
  $ cd ..
  $ catkin_make
  ```
## modifications 

Go to robotiq/robotiq_description/urdf/robotiq_85_gripper.transmission.xacro

Change hardware interface from PositionJointInterface to -> EffortJointInterface

should look like this: <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>



## Simulation in Gazebo

To simulate the robot launch the following:
  ```
  $ roslaunch robot_gazebo **SELECT**.launch

different launch files **SELECT**.launch 

HOME_setup.launch -> launched a ur5 robot on a linear track in the ISS

ur5_above_manipulation.launch nut:=false -> launches ur5 robot with track mounted to    cieling. endeffector is a gripper

ur5_above_manipulation.launch nut:=true -> launches ur5 robot with track mounted to    cieling. endeffector is a nutdriver

