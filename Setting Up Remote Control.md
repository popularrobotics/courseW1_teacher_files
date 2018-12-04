# Setting Up Remote Control
This tutorial shows you how to set static IP, connect your phone or laptop to the robot wirelessly, and control the motors remotely.

## STEPS

### 1. Remote Control the Robot With an Automatic IP Address
1. Connect the robot to the Wifi network you want to control it over
2. View the Robot's Automatic IP Address.  
![step 1 screenshot](/tutorial_pics/connection_info.png)  
![step 2 screenshot](/tutorial_pics/detailed_connection_information.png)  
3. Make sure both the robot and the device you'll be using to remote control the robot (e.g. laptop, smartphone, etc.) are connected to the same Wifi network.
4. Run (Execute) the 'course_w1_remote_control.py' file under the 'src' folder. When it shows 'Ready' in the terminal, you could proceed to the next step.
5. Open a browser on your device, in the address field type in the robot's automatic IP address, and end it with `:9093` (the complete URL should look something like `192.168.0.123:9093`)
6. Once the webpage loads, put the robot's automatic IP address in the box on the left and hit "connect"
7. If it shows "connected", voilà! Now you can now control the robot in your browser!  

Note: The router **HAS** to be connected to the Internet for the romote control to work!

### 2. Set a Static IP for the Robot Based On Its Automatic IP
1. Connect the robot to a Wifi network, click on the network icon at the task bar, and choose **Edit Connections...**  
![step 1 screenshot](/tutorial_pics/edit_connections.png)
2. Choose the Wifi you're currently connected to, and click **Edit**.  
![step 2 screenshot](/tutorial_pics/edit_current_connection.png)
3. Click on the **IPv4 Settings** tab, and in the **Method:** drop-down menu, choose **Manual**.  
![step 3 screenshot](/tutorial_pics/manual.png)
4. Click **Add**, and add an IP address of your choice (e.g. `192.168.0.123`), hit 'enter' on your keyboard and there will be a Netmask number generated automatically.  
![step 4 screenshot](/tutorial_pics/add.png)  
Note: 
    - Each device/robot that connects to the same router (Wifi network) MUST have a DIFFERENT IP address.
    - You need to choose an IP address that the router accepts. We recommend setting an IP address where the first 3 numbers are the same as the automatic IP address's, and the last number a bit bigger than the number of devices connected to this Wifi network. For instance, if the automatic IP address is `192.168.0.50` then set the static IP address as `192.168.0.*` where `*` is a number between 51 and 255. If the IP address you set is taken by other devices on the network, use a bigger (but no bigger than 255) number for `*`.
    - The router **HAS** to be connected to the Internet for the romote control to work!
    - The router **HAS** to be able to handle static IPs. But unless you configured it specifically not to accept static IPs, it should be able to.
5. Click **Save**, reconnect to the Wifi network, and done.  
![step 5 screenshot](/tutorial_pics/save.png)

### 3. Make Robot Automatically Controllable Upon Startup
Please read and follow the instructions in **Running a Script Automatically Upon Startup** tutorial in this course. But replace **course_w1.py** with **course_w1_remote_control.py** in the `robot_startup.sh` file.

### 4. Connect To the Robot and Remote Control the Motors
1. Make sure both the robot and the device you'll be using to remote control the robot (e.g. laptop, smartphone, etc.) are connected to the same Wifi network.
2. Run (Execute) the 'course_w1_remote_control.py' file under the 'src' folder. When it shows 'Ready' in the terminal, you could proceed to the next step.
3. Open a browser on your device, in the address field type in the static IP address you set for the robot, and end it with `:9093` (the complete URL should look something like `192.168.0.123:9093`)
4. Once the webpage loads, put the robot's static IP address in the box on the left and hit "connect"
5. If it shows "connected", voilà! Now you can now control the robot in your browser!  

---

## Copyright
All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without prior written permission from Popular Robotics, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law. For permission requests, contact Popular Robotics directly.

---

Edited by Lyuzhou Zhuang on 11/29/2018