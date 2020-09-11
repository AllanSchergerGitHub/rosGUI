# ROS_GUI

Put this code within your ROS directory or it may not work properly.

This GUI will work with any and all types of terminal commands; it is not limited to just working with ROS.

## How to start this code

from command line `python ROS_GUI.py` and press the enter key.

note: the other files in this directory are non-working drafts of different approaches and ideas.

## There are 3 manual entries that need to be added for each launch file you wish to control (title, working_directory, and command):

example:

title1 = "roslaunch rover_desc_pkg move_base_controller.launch"  # title shows on the button - it can be any helpful text

working_directory1 = "--working-directory=/home/allan/rover_ros_yuthika_vio/RoverYuthika"

command1 = "roslaunch rover_desc_pkg move_base_controller.launch"  # package and launch_file_name
