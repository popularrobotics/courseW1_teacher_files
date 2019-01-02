# Ubuntu & ROS Basics


## What is Ubuntu?
Ubuntu is a free and open-source operating system and Linux distribution based on Debian. Ubuntu is offered in three official editions: Ubuntu Desktop for personal computers, Ubuntu Server for servers and the cloud, and Ubuntu Core for Internet of things devices and robots. In this course we're using a lightweight version of **Ubuntu 16.04 (LXDE)**, running on Raspberry Pi 3, with ROS Kinetic installed.


## What is ROS?
Robot Operating System (ROS) is a collection of software frameworks for robot software development, providing operating system-like functionality on a heterogeneous computer cluster. In this course we're using **ROS Kinetic**.


## Installing Ubuntu + ROS Kinetic on the Raspberry Pi 3
If you haven't installed Ubuntu and ROS on your Raspberry Pi 3, please follow the instructions in the "Setting Up Your RPi Board" tutorial in this course.


## Basic Ubuntu & ROS Commands
Note:  
- Commands in the text below are to be typed and executed in a Terminal, unless instructed otherwise.
- If you've cloned the `courseW1_ws` repository, then the folder itself and all files in it make up a complete ROS workspace. You could `rosrun` the nodes in it through a terminal, or follow the steps below to create another ROS workspace, and copy the nodes into your new workspace (see STEP **Adding New Python Scripts (nodes) into an Existing Package** below). We recommend the later approach so that by going through the tutorial, you learn the basics of ROS.
- If you're creating another ROS workspcace, you may replace `courseW1_ws` and `robot_control` in **all** code below with your own defined project name and package name. But remember to keep them **consistent** throughout this course.

### Update the Repository List of Downloadable Programs
In a terminal, run the following command
```
$ sudo apt-get update
```

### Setting up ROS on a New Machine
1. [Install ROS](http://wiki.ros.org/kinetic/Installation/Ubuntu) if it's **NOT** already installed. If you've followed the "Setting Up Your RPi Board" tutorial in this course, then ROS is already installed in your system.
2. Managing Your Environment:  
    ```
    $ printenv | grep ROS
    ```
	Add the following line to the end of the hidden .bashrc file (/home/ubuntu) if it's not already there. This file runs every time you start a new terminal (Ctrl + Shift + T)  
	`source /opt/ros/kinetic/setup.bash` 

[more details](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

### Creating a ROS Workspace (project)
1. build a [catkin workspace](http://wiki.ros.org/catkin/workspaces):
    ```
    $ mkdir -p ~/courseW1_ws/src
    $ cd ~/courseW1_ws/
    $ catkin_make
    ```
2. Add the following line to the end of the hidden .bashrc file, and comment out the lines for other projects:  
    `source /home/ubuntu(youruser)/courseW1_ws/devel/setup.bash`
3. To make sure your workspace is properly overlayed by the setup script, make sure ROS_PACKAGE_PATH environment variable includes the directory you're in (echo command here shows whatever is in ROS_PACKAGE_PATH). Start a new terminal, and type in the following command:
    ```
    $ echo $ROS_PACKAGE_PATH
    ```
    And it should return something like: `/home/youruser/catkin_ws/src:/opt/ros/kinetic/share`

### Creating and Building a ROS Package
1. Change to the source space directory of the catkin workspace 
    ```
    $ cd ~/courseW1_ws/src
    ```
2. Use the `catkin_create_pkg` script to create a new package called ‘robot_control’ which depends on std_msgs, roscpp, and rospy
    ```
	$ catkin_create_pkg robot_control std_msgs rospy roscpp
    ```
3. Build the packages in the catkin workspace and source the setup file
    ```
	$ cd ~/courseW1_ws
	$ catkin_make
	$ source devel/setup.bash
    ```
[more details](http://wiki.ros.org/ROS/Tutorials/CreatingPackage)

### Creating and Running a Python File(node) in ROS
1. Set package path
    ```
	$ roscd robot_control
    ```
2. Create a folder to store your scripts (e.g. a “src” folder)
	```
	$ mkdir src
	$ cd src
    ```
3. Create a python script under the foder you just created (or download an existing python file with the following command, the file downloaded is called **talker.py**)
    ```
	$ wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
    ```
    and make it executable
    ```
	$ chmod +x talker.py
    ```
4. Build the node(s)
    ```
	$ cd ~/courseW1_ws
	$ catkin_make
    ```
5. Before you run a node, make sure that a roscore is up and running, make sure you have sourced your workspace's setup.bash file after calling catkin_make but before trying to use your applications
    ```
	$ roscore
	$ cd ~/courseW1_ws
	$ source devel/setup.bash
    ```
6. Run your code!
    ```
	$ rosrun robot_control talker.py
    ```

### Adding New Python Scripts (nodes) into an Existing Package (e.g. under the **src** folder)
Run the following commands **after** you added the new python files
```
$ cd ~/courseW1_ws  
$ chmod +x file_path/new_script.py
$ catkin_make
$ roscore
$ source devel/setup.bash
```
Now you can rosrun the new script
```
$ rosrun robot_control new_script.py
```

### When Significant Changes Are Made Within the Workspace (e.g. deleting a package)
Delete ‘build’ and ‘devel’ folders under the ‘courseW1_ws’ folder and rerun
```
$ catkin_make
```

### Quick Tips
- To make a node executable
```
$ chmod +x file_path/new_script.py
```
- Building a node
```
$ cd ~/courseW1_ws
$ catkin_make
```
- Before you run a node
```
$ roscore
$ cd ~/courseW1_ws
$ source devel/setup.bash
```

### Trouble shooting
If roscd says something similar to `roscd: No such package/stack 'beginner_tutorials'`, you will need to source the environment setup file like you did at the end of the [create_a_workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) tutorial.

### Understanding ROS Workspaces, Packages, and Nodes
Nodes are executables (functions) that can communicate with each other through messages on topics or services; packages are clusters of nodes, like folders, but they can also share libraries; workspaces (projects) are groups of packages.

## Reference
- [Ubuntu Official Site](https://www.ubuntu.com/global)
- [Ubuntu Tutorials](https://tutorials.ubuntu.com)
- [ROS Beginner Tutorials](http://wiki.ros.org/ROS/Tutorials)
- [Ubuntu + ROS Disk Images for RPi 3](https://downloads.ubiquityrobotics.com)
- [Installing ROS Kinetic on Ubuntu](http://wiki.ros.org/kinetic/Installation/Ubuntu)

---

## Copyright
All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without prior written permission from Popular Robotics, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law. For permission requests, contact Popular Robotics directly.

---

Edited by Lyuzhou Zhuang on 12/4/2018