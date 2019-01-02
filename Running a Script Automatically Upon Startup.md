# Running a Script Automatically Upon Startup
This tutorial will show you how to configure the system to run a script automatically upon system startup, which will be quite useful at the last session of this course - autonomous driving challenge.  

## NOTE
- If you've created another ROS workspcace other than `courseW1_ws` and want to work on that new workspace, replace `courseW1_ws` and `robot_control` in **all** code below with your own defined project name and package name, and keep them **consistent** throughout this course.
- [sudo] password for ubuntu is: `ubuntu`

## STEPS

### 1. Install `gnome-terminal` and `gedit`
Open a Terminal and run the following command  
Note: [sudo] password for ubuntu is: `ubuntu`
```
$ sudo apt-get update
$ sudo apt-get install gnome-terminal gedit
```

### 2. Create a Startup Bash File
Create a startup bash file called `robot_startup.sh` under the workspace folder `courseW1_ws`, inside the file add the following script and save it. If you want to auto-run another script, just change the file name (in this example it's `course_w1.py` in the last line of the script below) to that new script file name in the last command below, and the file path if necessary (in this example it's `cd /home/ubuntu/courseW1_ws/src/robot_control/src` in the last line of the script below).
```
#!/bin/bash
workspace_path=/home/ubuntu/courseW1_ws 
sudo chmod 777 /dev/tty*
source $workspace_path/devel/setup.bash
#chmod +x $workspace_path/script/*
gnome-terminal -x bash -c "roscore" 
gnome-terminal -x bash -c "sleep 2 && cd /home/ubuntu/courseW1_ws/src/robot_control/src && rosrun robot_control course_w1.py" &
```

### 3. Test the Bash File
To test whether the sh file is working correctly, you can run it in a terminal.  
Note: Replace the 'path_to_file' in the following example with the actual path to file (in this example, it's `courseW1_ws`).  
1. Make this bash file executable:
    ```
    $ cd ~/courseW1_ws/
    $ chmod 777 robot_startup.sh
    ```
2. Execute it:
    ```
    $ ~/path_to_file/robot_startup.sh
    ```

### 4. Make the bash file run upon startup
In the terminal, run the following command to create a new file and open it
```
$ sudo gedit /usr/share/applications/autoScripts.desktop
```
In the file, put in the following scripts and save
```
[Desktop Entry]
Name=autoScripts
Exec=/home/ubuntu/courseW1_ws/robot_startup.sh
Type=Application
Terminal=False
```
In the terminal, run the following 
```
$ sudo cp /usr/share/applications/autoScripts.desktop /etc/xdg/autostart
```

### 5. Enable Auto-login Upon Startup
In the terminal, run the following command to create a new file and open it
```
$ sudo gedit /etc/lightdm/lightdm.conf
```
In the file, add the following scripts and save
```
[SeatDefaults]
autologin-user=ubuntu
autologin-user-timeout=0
user-session=Lubuntu
greeter-session=lightdm-gtk-greeter
```
[reference](https://www.smarthomebeginner.com/enable-lubuntu-auto-login/)

### 6. All done! 
The program should auto-run next time you power on the robot!

---

## Copyright
All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without prior written permission from Popular Robotics, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law. For permission requests, contact Popular Robotics directly.

---

Edited by Lyuzhou Zhuang on 12/5/2018