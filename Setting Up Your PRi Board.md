# Setting Up Your PRi Board

This tutorial covers the steps of installing Ubuntu 16.04 (LXDE) and ROS Kinetic on the Raspberry Pi 3 Board. If you're not sure whether you have the right system installed on your RPi board, simply follow the instructions below to (re)install the system.

## STEPS
### 1. Download the System Image
Download the SD Card Image with Ubuntu 16.04 (LXDE) and ROS Kinetic installed for Raspberry Pi 3 [**here**](https://cdn.ubiquityrobotics.net/2018-11-15-ubiquity-xenial-lxde-raspberry-pi.img.xz).


### 2. Burn the System Image Onto a Micro SD Card (16GB+)
- Ubuntu users  
Under Ubuntu Linux we recommend using the **GNOME** Disks tool to flash images onto the Micro SD card as it has native support for xz compressed images. If you haven't installed it, simply run `sudo apt install gnome-disk-utility`. Then you can double click on the downloaded image file, the GNOME Disks tool will automatically come up, and you can direct it to expand the image on to an SD card drive attached to your computer.

- Windows or Mac users  
On Windows or Mac we recommend using **etcher** to flash images onto SD cards. You may download it [**here**](https://www.balena.io/etcher/).

After you burn the system onto the Micro SD card, plug it into the RPi board. Connect the RPi to power source, and turn it on. It is recommended that you connect a display to the board via HDMI cable so you could see what's happening, and connect a keyboard and mouse to control it. If you don't have these, please see the next step.  

Note: the default password for the system is `ubuntu`


### 3. Accessing the RPi Remotely
If you don't have a display, keyboard and mouse connected to the RPi board directly, you may access it romotely from another computer via SSH:  
1. When the Raspberry Pi boots for the first time (may take some time), it comes up as a Wifi access point. The SSID is `ubiquityrobotXXXX` where XXXX is part of the MAC address. The wifi password is `robotseverywhere`. Connect to this Wifi from another computer.
2. Once connected, open a Terminal on the other computer, run this command: `ssh ubuntu@10.42.0.1` and enter password `ubuntu` at the prompt.
3. Now you can run commands in the Terminal on the other computer as if you run them in the Terminal on the RPi board.  

Note:  
If you've connected to other robots using the same `ssh ubuntu@10.42.0.1` command before on the same device, you may need to first clear everything in the **known_hosts** file under the **.ssh** folder on your device, then you could ssh to a new robot with this command.

## Reference
- [Ubiquity Robotics Raspberry Pi Images](https://downloads.ubiquityrobotics.com/pi.html)
- [etcher - Flash OS images to SD cards](https://www.balena.io/etcher/)

---

## Copyright
All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without prior written permission from Popular Robotics, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law. For permission requests, contact Popular Robotics directly.

---

Edited by Lyuzhou Zhuang on 11/29/2018