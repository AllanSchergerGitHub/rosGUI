#! /usr/bin/python
# inspired by http://www.linuxjournal.com/article/8005?page=0,2
# https://itectec.com/ubuntu/ubuntu-how-to-send-commands-to-specific-terminal-windows/
# https://answers.ros.org/question/44709/how-can-i-automate-my-ros-work-session-environment/
# http://manpages.ubuntu.com/manpages/trusty/man1/xdotool.1.html
# https://askubuntu.com/questions/641683/how-can-i-send-commands-to-specific-terminal-windows
# https://gist.github.com/alavarre/4893b05c21c6be210513a072b6fe782d
# https://github.com/ChickenProp/set-window-title/blob/master/set-window-title
# https://stackoverflow.com/questions/21563525/how-to-manipulate-a-window-in-linux
# https://unix.stackexchange.com/questions/154546/how-to-get-window-id-from-xdotool-window-stack

import subprocess
import tkinter as tk
import time

root = tk.Tk()

canvas1 = tk.Canvas(root, width=600, height=500, bg='gray90', relief='raised')
canvas1.pack()
windowid1 = ''
windowid2 = ''


def roslaunch_move_base_controller():
    global windowid1
    subprocess.call(["xdotool", "windowfocus", windowid1])
    subprocess.check_output(["xdotool", "type", ". devel/setup.sh\n"])
    time.sleep(1)
    subprocess.check_output(["xdotool", "type", "roslaunch rover_desc_pkg move_base_controller.launch\n"])


def roslaunch_start_navsat():
    global windowid2
    subprocess.call(["xdotool", "windowfocus", windowid2])
    subprocess.check_output(["xdotool", "type", ". devel/setup.sh\n"])
    time.sleep(1)
    subprocess.check_output(["xdotool", "type", "roslaunch rover_gazebo_control start_navsat.launch\n"])


def OpenAllDesiredTerminals():
    # create terminals
    global windowid1
    global windowid2
    title1 = "roslaunch rover_desc_pkg move_base_controller.launch"
    subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=100x20+450+20",
                     "--working-directory=/home/allan/rover_ros_yuthika_vio/RoverYuthika"])
    time.sleep(2)
    # assumes focus stays on window that was just created
    # can also run `xdotool getactivewindow` from command line to get the window id.
    # xwininfo -int will give info about the window but it requires you to mouse click on the desired window first.
    windowid1 = subprocess.check_output(["xdotool", "getactivewindow"])
    print("windowid1", windowid1.decode())


    title2 = "roslaunch rover_gazebo_control start_navsat.launch"
    subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=100x20+550+500",
                     "--working-directory=/home/allan/rover_ros_yuthika_vio/RoverYuthika"])
    time.sleep(2)
    # assumes focus stays on window that was just created
    # can also run `xdotool getactivewindow` from command line to get the window id.
    # xwininfo -int will give info about the window but it requires you to mouse click on the desired window first.
    windowid2 = subprocess.check_output(["xdotool", "getactivewindow"])
    print("windowid2", windowid2.decode())


button1 = tk.Button(text=' Step 1: Open Terminal Windows    ', command=OpenAllDesiredTerminals, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))

button2 = tk.Button(text=' Step 2: roslaunch_move_base_controller  ', command=roslaunch_move_base_controller, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))

button3 = tk.Button(text=' Step 3: roslaunch_start_navsat  ', command=roslaunch_start_navsat, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))

canvas1.create_window(250, 100, window=button1)
canvas1.create_window(250, 150, window=button2)
canvas1.create_window(250, 200, window=button3)

root.mainloop()