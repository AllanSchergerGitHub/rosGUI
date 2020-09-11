#! /usr/bin/python

# this is the best working example as of Sept 9 2020 - allanscherger@hotmail.com

# alternative approach:
# http://wiki.ros.org/roslaunch/API%20Usage

# inspired by:
# http://www.linuxjournal.com/article/8005?page=0,2
# https://itectec.com/ubuntu/ubuntu-how-to-send-commands-to-specific-terminal-windows/
# https://answers.ros.org/question/44709/how-can-i-automate-my-ros-work-session-environment/
# http://manpages.ubuntu.com/manpages/trusty/man1/xdotool.1.html
# https://askubuntu.com/questions/641683/how-can-i-send-commands-to-specific-terminal-windows
# https://gist.github.com/alavarre/4893b05c21c6be210513a072b6fe782d
# https://github.com/ChickenProp/set-window-title/blob/master/set-window-title
# https://stackoverflow.com/questions/21563525/how-to-manipulate-a-window-in-linux
# https://unix.stackexchange.com/questions/154546/how-to-get-window-id-from-xdotool-window-stack

import subprocess
import time
import tkinter as tk

root = tk.Tk()
root.title('ROS GUI')

canvas1 = tk.Canvas(root, width=600, height=500, bg='gray90', relief='raised')
canvas1.pack(side='left')

canvas2 = tk.Canvas(root, width=400, height=500, bg='gray90', relief='raised')
canvas2.pack(side='right')

windowid1 = ''
windowid2 = ''

title1 = "roslaunch rover_desc_pkg move_base_controller.launch"  # title shows on the button - it can be any helpful text
working_directory1 = "--working-directory=/home/allan/rover_ros_yuthika_vio/RoverYuthika"
command1 = "roslaunch rover_desc_pkg move_base_controller.launch"  # package and launch_file_name

title2 = "roslaunch rover_gazebo_control start_navsat.launch"  # title shows on the button - it can be any helpful text
working_directory2 = "--working-directory=/home/allan/rover_ros_yuthika_vio/RoverYuthika"
command2 = "roslaunch rover_gazebo_control start_navsat.launch"  # package and launch_file_name

title3 = "Catkin Clean"  # title shows on the button - it can be any helpful text
directory3 = "/rover_ros_yuthika_vio/RoverYuthika"
command3 = ["catkin clean", "placeholder"]

title4 = "Catkin_Make"  # title shows on the button - it can be any helpful text
directory4 = "/rover_ros_yuthika_vio/RoverYuthika"
command4 = ["catkin_make", "placeholder"]


def command1_method():
    global windowid1
    global command1
    subprocess.call(["xdotool", "windowfocus", windowid1])
    subprocess.check_output(["xdotool", "type", ". devel/setup.sh\n"])
    time.sleep(1)
    subprocess.call(["xdotool", "windowfocus", windowid1])
    subprocess.check_output(["xdotool", "type", command1 + "\n"])


def command2_method():
    global windowid2
    global command2
    subprocess.call(["xdotool", "windowfocus", windowid2])
    subprocess.check_output(["xdotool", "type", ". devel/setup.sh\n"])
    time.sleep(1)
    subprocess.call(["xdotool", "windowfocus", windowid2])
    subprocess.check_output(["xdotool", "type", command2 + "\n"])

    # time.sleep(1)
    # this code is an attempt at closing the terminal but it doesn't work
    # subprocess.call(["xdotool", "windowactivate", windowid2])
    # subprocess.check_output(["xdotool",  "alt+f4" + "\n"])


def command3_method():
    global windowid1
    global command3
    global directory3
    subprocess.call(["xdotool", "windowfocus", windowid1])
    subprocess.check_output(["xdotool", "type", "cd ~"+directory3+"\n"])
    subprocess.check_output(["xdotool", "type", ". devel/setup.sh\n"])
    time.sleep(1)
    subprocess.call(["xdotool", "windowfocus", windowid1])
    subprocess.check_output(["xdotool", "type", command3[0] + "\n"])
    # subprocess.check_output(["xdotool", "type", command3[1] + "\n"])


def command4_method():
    global windowid1
    global command4
    global directory4
    subprocess.call(["xdotool", "windowfocus", windowid1])
    subprocess.check_output(["xdotool", "type", "cd ~"+directory3+"\n"])
    # subprocess.check_output(["xdotool", "type", ". devel/setup.sh\n"])
    time.sleep(1)
    subprocess.call(["xdotool", "windowfocus", windowid1])
    subprocess.check_output(["xdotool", "type", command4[0] + "\n"])
    # subprocess.check_output(["xdotool", "type", command3[1] + "\n"])


def close_window(windowID):
    print("stub")


def OpenAllDesiredTerminals():
    # create terminals
    global windowid1
    global windowid2
    global working_directory1
    global working_directory2

    subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=100x20+450+20",
                     working_directory1])
    time.sleep(2)
    # assumes focus stays on window that was just created
    # can also run `xdotool getactivewindow` from command line to get the window id.
    # xwininfo -int will give info about the window but it requires you to mouse click on the desired window first.
    # xprop within a terminal will give a lot of info about that window.
    windowid1 = subprocess.check_output(["xdotool", "getactivewindow"])
    print("windowid1", windowid1.decode())

    subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=100x20+550+500",
                     working_directory2])
    time.sleep(2)
    # assumes focus stays on window that was just created
    # can also run `xdotool getactivewindow` from command line to get the window id.
    # xwininfo -int will give info about the window but it requires you to mouse click on the desired window first.
    windowid2 = subprocess.check_output(["xdotool", "getactivewindow"])
    print("windowid2", windowid2.decode())


buttonA = tk.Button(text=' Step 1: Open Terminal Windows', command=OpenAllDesiredTerminals, bg='green', fg='white',
                    font=('helvetica', 11, 'bold'))

button1 = tk.Button(text=' Step 2: ' + title1, command=command1_method, bg='green', fg='white',
                    font=('helvetica', 11, 'bold'))

button2 = tk.Button(text=' Step 3: ' + title2, command=command2_method, bg='green', fg='white',
                    font=('helvetica', 11, 'bold'))

button3 = tk.Button(text=' Catkin Clean: ' + title3, command=command3_method, bg='green', fg='white',
                    font=('helvetica', 11, 'bold'))

button4 = tk.Button(text=' Catkin_Make: ' + title4, command=command4_method, bg='green', fg='white',
                    font=('helvetica', 11, 'bold'))

# print("len1", len(title1))
# print("len2", len(title2))

buttonx_orig = 80
buttongap = 40

canvas1.create_window(151, buttonx_orig, window=buttonA)
# canvas1.create_window(350-len(command2), 130, window=button1)
# canvas1.create_window(350-len(command1)-15, 180, window=button2)

buttonx = buttonx_orig + buttongap
canvas1.create_window(213+len(title1), buttonx, window=button1)
buttonx = buttonx + buttongap
canvas1.create_window(200+len(title2), buttonx, window=button2)
buttonx = buttonx + buttongap

buttonx = buttonx_orig
canvas2.create_window(200, buttonx, window=button3)
buttonx = buttonx + buttongap
canvas2.create_window(200, buttonx, window=button4)

root.mainloop()