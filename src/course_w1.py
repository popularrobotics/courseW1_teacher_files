#!/usr/bin/env python
# Popular Robotics CourseW1 Template
# Last edited by Lyuzhou Zhuang on 11/20/2018

"""
# Please read ALL comments in this script carefully as they contain useful information
# and could help you avoid a lot of potential bugs.
#
# This file is the courseW1 template. It contains python basics and test functions
# for students to refer to. Student can add their own functions in this file.
#
# This is the ONLY file in the project students could edit. Also students should NOT
# touch any existing functions other than student_function().
# But students can always add new functions.
#
# The imported course_w1_cheatsheet is the teacher's answer. Students should try to
# work on their own before taking a look at the cheatsheet. And students should NOT
# use any functions from cheatsheet for the challenge.
#
# Copyright
#   All rights reserved. No part of this script may be reproduced, distributed, or transmitted in any 
#   form or by any means, including photocopying, recording, or other electronic or mechanical methods, 
#   without prior written permission from Popular Robotics, except in the case of brief quotations embodied 
#   in critical reviews and certain other noncommercial uses permitted by copyright law. 
#   For permission requests, contact Popular Robotics directly.
#
# PREREQUISITES
#   Tornado Web Server for Python
#
# TROUBLESHOOTING:
#   Don't use Ctrl+Z to stop the program, use Ctrl+c.
#	If you use Ctrl+Z, it will not close the socket and you won't be able to run the program the next time.
#	If you get the following error:
#		"socket.error: [Error 98] Address already in use "
#	Run this on the terminal:
#		"sudo netstat -ap |grep:9093"
#	Note down the PID of the process running it
#	And kill that process using:
#		"kill pid"
#	If it does not work use:
#		"kill -9 pid"
#	If the error does not go away, try changing the port number '9093' both in the client and server code
"""

# The below commands imports other python files (modules) to be used in this script.
import Basic_Motor_Control_Code as Motor
import Three_Ultrasonic_Sensors as Ultrasonic
import course_w1_cheatsheet as Cheatsheet
import time


# ----- example functions below -----

def python_basics():

    # This function contains basic python syntax and statements for you to refer to

    # Below is a print command, it prints whatever string after the 'print' keyword
    print "Hello, World!"
    # Anything behind '# ' is a comment and will be ignored at runtime.
    # --------------------------------------
    # Defining a boolean, which can only be either 'True' or 'False'
    boolean = True
    # Below is an if statement
    if boolean: # If the condition is True, do the following
        print "True"
    else:   # Otherwise, do the following
        print "False"
    # --------------------------------------
    # Calculation with line break, '\' indicates a line break
    total = 1 + \
            2 + \
            3
    # --------------------------------------
    # Defining a list
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday']
    # --------------------------------------
    # Defining strings
    word = 'word'
    sentence = "This is a sentence."
    # Defining a string with in multiple lines
    paragraph = """This is a paragraph.
                It has multiple lines."""
    # --------------------------------------
    # Defining a variable, list, tuple or dictionary
    var = 0
    lst = [1, 2, 3, 4]
    tuple = (1, 2, 3)
    dict = {'one': 1, 'two': 2}
    # --------------------------------------
    # Below is a typical for loop
    # range(a, b) generates a list from a to b-1 with an increment of 1
    for i in range(1, 3):   # when i == 1 and i == 2, print i
        print i
    # --------------------------------------
    i = 0
    # Below is a typical while loop
    while i < 10:   # while condition is True, do the following
        if i == 3:
            i += 1
            continue    # skip the rest of the commands in this iteration and start the next iteration immediately
        if i == 5:
            break   # exit the while loop immediately
        print i
        i += 1  # i = i + 1
    else:   # Otherwise, do the following
        print "While loop ended."
    # --------------------------------------


def test_wheel_motors():    # test to see if wheel motors function properly
    Motor.vehicle_move_forward(50, 0.5)   # arguments: speed (between 0 and 100), duration (seconds)
    # Note: Once the motors are set to a certain mode (e.g. move_forward),
    # it keeps it until a new command changes its mode. So the duration can be set to 0.
    # If the duration is greater than 0, it ensures that the motors keep this state for
    # the amount of time you set, but you can't run any other commands including changing
    # motor speed or invoke ultrasonic sensors. This applies to all function calls below
    # that has a duration parameter.
    # Motor.vehicle_move_forward(50, 0.5) means calling the 'vehicle_move_forward()' function
    # from the Motor module that was imported at the beginning of the script.
    Motor.vehicle_stop_moving_for(.2)   # argument: duration (seconds)
    Motor.vehicle_move_backward(50, 0.5)    # arguments: speed (between 0 and 100), duration (seconds)
    Motor.vehicle_stop_moving_for(.2)
    Motor.vehicle_turn_left(50, 0.5)    # arguments: speed (between 0 and 100), duration (seconds)
    Motor.vehicle_stop_moving_for(.2)
    Motor.vehicle_turn_right(50, 0.5)   # arguments: speed (between 0 and 100), duration (seconds)
    Motor.vehicle_stop_moving_for(.2)


def test_ultrasonic_sensors():  # test to see if ultrasonic sensors function properly
    try:
        Ultrasonic.loop_read_distance()
        # Note: when this function is called, the program does nothing else
        # but keeps reading data from the ultrasonic sensors
        # until you kill the running program
    except KeyboardInterrupt:
        Ultrasonic.destroy()

# ----- example functions above -----


# ***** student edits start *****
# students define their own functions here.

def student_function():
    #
    # You could edit and this function freely and try out your ideas.
    # You could also add new functions outside of this function and call it here.
    # Please read other functions in this file to learn more about python syntax
    # and how to call functions from other modules.
    # You should not change any code outside of this function.
    #
    # Below are some example function calls
    test_wheel_motors()  # This function is to test if the wheel motors work as expected.
    # You could comment it out if they do.
    test_ultrasonic_sensors()   # This function is to test if the ultrasonic sensors work as expected.
    # You SHOULD comment it out if they do.
    dis_f = Ultrasonic.read_distance(0)
    # arguments: 0: read from front ultrasonic sensor;
    # 1: read from right ultrasonic sensor
    # 2: read from left ultrasonic sensor
    print 'front distance: ', dis_f, 'cm'   # Print out the distance
    Motor.vehicle_move_forward(50, 0.5)  # arguments: speed (between 0 and 100), duration (seconds)
    # Note: Once the motors are set to a certain mode (e.g. move_forward),
    # it keeps it until a new command changes its mode. So the duration can be set to 0.
    # If the duration is greater than 0, it ensures that the motors keep this state for
    # the amount of time you set, but you can't run any other commands including changing
    # motor speed or invoke ultrasonic sensors. This applies to all motor function calls
    # that has a duration parameter.
    # Motor.vehicle_move_forward(50, 0.5) means calling the 'vehicle_move_forward()' function
    # from the Motor module that was imported at the beginning of the script.
    Motor.vehicle_stop_moving_for(0)  # argument: duration (seconds)
    pass    # If you haven't written any valid commands in a function, put 'pass' as a placeholder
    # Now unleash your creativity and write more code below ;)
    #

# ***** student edits end *****


# ----- main function below -----

if __name__ == "__main__":  # call any function below
    student_function()

# ----- main function above -----



