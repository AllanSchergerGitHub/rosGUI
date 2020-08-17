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

import os
import subprocess
import tkinter as tk
import time
from Xlib import X, display
#import xdotool

root = tk.Tk()

canvas1 = tk.Canvas(root, width=600, height=500, bg='gray90', relief='raised')
canvas1.pack()
activeWinTitle = ''
windowid1 = ''

def TrackMouseCoordinates():
    # useful for finding location of open terminal windows
    loops = 0
    while True:
        d = display.Display()
        s = d.screen()
        root1 = s.root
        a = root1.query_pointer()
        b = a._data
        print (b["root_x"], b["root_y"])
        d.sync()
        time.sleep(.5)
        loops += 1
        if loops > 10:
            break


def sendKeystrokesToWindow_():
    sendKeystrokesToWindow(activeWinTitle, "ls\n")


def sendKeystrokesToWindow(windowID, keystrokes):
    # print "sending command %s " %command
    print("windowID", windowID)
    print("keystrokes =", keystrokes)
    # subprocess.call(["xdotool", "key", "%s" % command ])
    y = subprocess.call(["xdotool", "windowfocus", "54577595"])
    # subprocess.call(["xdotool", "type", "--window", windowID, keystrokes])
    subprocess.call(["xdotool", "type", keystrokes])


def ReturnActiveTerminal():
    # click on a terminal to activate it (activating sam terminal at 705,37)
    # subprocess.call(["xdotool", "mousemove", "705", "37", "click", "1"])
    subprocess.call(["xdotool", "mousemove", "2122", "164", "click", "1"])
    activeWinTitle = GetActiveWindowTitle()
    print('Active window title: ', activeWinTitle)
    return activeWinTitle


def roslaunch_move_base_controller():
    global windowid1
    subprocess.call(["xdotool", "windowfocus", windowid1])
    subprocess.check_output(["xdotool", "type", ". devel/setup.sh\n"])
    time.sleep(1)
    subprocess.check_output(["xdotool", "type", "roslaunch rover_desc_pkg move_base_controller.launch\n"])


def OpenAllDesiredTerminals():
    # create terminals
    global activeWinTitle
    global windowid1
    # geometry is widthxheight+x+y   50x10+1935+20
    # subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=100x10+1935+20", "--working-directory=sam"])
    title = "roslaunch rover_desc_pkg move_base_controller.launch"
    subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=100x10+1935+20",
                     "--working-directory=/home/allan/rover_ros_yuthika_vio/RoverYuthika"])
    time.sleep(2)

    # assumes focus stays on window that was just created
    # can also run `xdotool getactivewindow` from command line to get the window id.
    # xwininfo -int will give info about the window but it requires you to mouse click on the desired window first.
    windowid1 = subprocess.check_output(["xdotool", "getactivewindow"])

    # subprocess.check_call(['xprop', '-id', windowid1,
    #                        '-format', '_NET_WM_VISIBLE_NAME', '8s',
    #                        '-set', '_NET_WM_VISIBLE_NAME', title])
    # subprocess.check_call(['xprop', '-id', windowid1,
    #                        '-format', '_NET_WM_NAME', '8s',
    #                        '-set', '_NET_WM_NAME', title])
    # subprocess.check_call(['xprop', '-id', windowid1,
    #                        '-format', 'WM_NAME', '8s',
    #                        '-set', 'WM_NAME', title])

    # subprocess.call(["xdotool", "search", "--name", ])


def GetActiveWindowTitle():
    return subprocess.Popen(["xprop", "-id", subprocess.Popen(
        ["xprop", "-root", "_NET_ACTIVE_WINDOW"], stdout=subprocess.PIPE).communicate()[0].strip().split()[-1], "WM_NAME"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).communicate()[0].strip().split(b'"', 1)[-1][:-1]


button1 = tk.Button(text='   Open Terminal Windows    ', command=OpenAllDesiredTerminals, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))

button2 = tk.Button(text='      Track Mouse Pos      ', command=TrackMouseCoordinates, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))

button3 = tk.Button(text='  ls in Terminal Window 1  ', command=sendKeystrokesToWindow_, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))

button4 = tk.Button(text=' step 1: roslaunch_move_base_controller  ', command=roslaunch_move_base_controller, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))

canvas1.create_window(250, 100, window=button1)
canvas1.create_window(250, 140, window=button2)
canvas1.create_window(250, 180, window=button3)
canvas1.create_window(250, 240, window=button4)

root.mainloop()