#! /usr/bin/python

# this is the best working example as of Sept 13 2020 - allanscherger@hotmail.com

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
from tkinter import *


class MainApplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        self.window_id1 = ''
        self.window_id2 = ''
        self.window_id3 = ''

        self.directory = "/home/allan/rover_ros_yuthika_vio/RoverYuthika"

        self.working_directory1 = "--working-directory=/home/allan/rover_ros_yuthika_vio/RoverYuthika"
        self.directory1 = self.directory  # this may need to be hard coded depending on the usage
        self.command1 = "roslaunch rover_desc_pkg move_base_controller.launch"  # package and launch_file_name

        self.working_directory2 = "--working-directory=/home/allan/rover_ros_yuthika_vio/RoverYuthika"
        self.directory2 = self.directory  # this may need to be hard coded depending on the usage
        self.command2 = "roslaunch rover_gazebo_control start_navsat.launch"  # package and launch_file_name

        self.working_directory3 = "--working-directory=/home/allan/rover_ros_yuthika_vio/RoverYuthika"
        self.directory3 = self.directory  # this may need to be hard coded depending on the usage
        self.command3 = "roslaunch rover_gazebo_control gps_waypoint_nav.launch"  # package and launch_file_name

        self.directory4 = "/home/allan/rover_ros_yuthika_vio/RoverYuthika"
        self.command4 = ["catkin clean", "placeholder"]

        self.directory5 = "/home/allan/rover_ros_yuthika_vio/RoverYuthika"
        self.command5 = ["catkin_make", "placeholder"]

    def init_window(self):
        self.master.title("ROS GUI")

        # title shows on the button - it can be any helpful text
        title1 = "roslaunch rover_desc_pkg move_base_controller.launch"
        title2 = "roslaunch rover_gazebo_control start_navsat.launch"
        title3 = "roslaunch rover_gazebo_control gps_waypoint_nav.launch"

        title4 = "Catkin Clean"
        title5 = "Catkin_Make"

        button_a = Button(text=' Step 1: Open Terminal Windows', command=self.callback_open_all_terminals,
                          bg='green', fg='white', font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button_a.grid(row=1, column=1, sticky='news')

        button1 = Button(text=' Step 2: ' + title1,
                         command=lambda: self.command_method(self.window_id1, self.directory1, self.command1),
                         bg='green', fg='white', font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button1.grid(row=4, column=1, sticky='news')

        button2 = Button(text=' Step 3: ' + title2,
                         command=lambda: self.command_method(self.window_id2, self.directory2, self.command2),
                         bg='green', fg='white', font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button2.grid(row=5, column=1, sticky='news')

        button2_1 = Button(text='Follow GPS Path: ' + title3,
                           command=lambda: self.command_method(self.window_id3, self.directory3, self.command3),
                           bg='green', fg='white', font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button2_1.grid(row=6, column=1, sticky='news')

        button3 = Button(text=' Catkin Clean: ' + title4, command=self.command4_method, bg='green', fg='white',
                         font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button3.grid(row=1, column=3, sticky='news')

        button4 = Button(text=' Catkin_Make: ' + title5, command=self.command5_method, bg='green', fg='white',
                         font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button4.grid(row=2, column=3, sticky='news')

        button5 = Button(text=' close_window #1 and Exit Program', command=lambda: self.close_terminal(self.window_id1),
                         bg='green', fg='white',
                         font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button5.grid(row=4, column=3, sticky='news')

        button6 = Button(text=' close_window #2 and Exit Program', command=lambda: self.close_terminal(self.window_id2),
                         bg='green', fg='white',
                         font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button6.grid(row=5, column=3, sticky='news')

        button7 = Button(text=' close_window #3 and Exit Program', command=lambda: self.close_terminal(self.window_id3),
                         bg='green', fg='white',
                         font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button7.grid(row=6, column=3, sticky='news')

        button8 = Button(text=' close all windows - Exit All Programs', command=self.close_all_terminals, bg='green',
                         fg='white',
                         font=('helvetica', 11, 'bold'), padx=5, pady=5)
        button8.grid(row=7, column=3, sticky='news')

    def command_method(self, window_id, directory, command):
        subprocess.call(["xdotool", "windowfocus", window_id])
        subprocess.check_output(["xdotool", "type", "cd " + directory + "\n"])
        subprocess.check_output(["xdotool", "type", ". devel/setup.sh\n"])
        time.sleep(1)
        subprocess.call(["xdotool", "windowfocus", window_id])
        subprocess.check_output(["xdotool", "type", command + "\n"])

    def command4_method(self):
        window_id = self.window_id1
        subprocess.call(["xdotool", "windowfocus", window_id])
        subprocess.check_output(["xdotool", "type", "cd " + self.directory4 + "\n"])
        subprocess.check_output(["xdotool", "type", ". devel/setup.sh\n"])
        time.sleep(1)
        subprocess.call(["xdotool", "windowfocus", window_id])
        subprocess.check_output(["xdotool", "type", self.command4[0] + "\n"])

    def command5_method(self):
        window_id = self.window_id1
        subprocess.call(["xdotool", "windowfocus", window_id])
        subprocess.check_output(["xdotool", "type", "cd " + self.directory5 + "\n"])
        time.sleep(1)
        subprocess.call(["xdotool", "windowfocus", window_id])
        subprocess.check_output(["xdotool", "type", self.command5[0] + "\n"])

    def close_terminal(self, window_id):
        try:
            subprocess.check_output(["xdotool", "windowclose", window_id])
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    def close_all_terminals(self):
        self.close_terminal(self.window_id1)
        self.close_terminal(self.window_id2)
        self.close_terminal(self.window_id3)

    def openterminal(self, working_directory, pos_x, pos_y):
        subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=100x20+450+20",
                         working_directory])
        time.sleep(0.75)
        # assumes focus stays on window that was just created
        # can also run `xdotool getactivewindow` from command line to get the window id.
        # xwininfo -int will give info about the window but it requires you to mouse click on the desired window first.
        # xprop within a terminal will give a lot of info about that window.
        window_id = subprocess.check_output(["xdotool", "getactivewindow"])
        subprocess.check_output(["xdotool", "windowmove", window_id, str(pos_x), str(pos_y)])
        print("window_id", window_id.decode(), window_id)
        return window_id

    def open_all_desired_terminals(self):
        # create terminals
        # last two numbers are the x,y position for terminal. x from left edge of screen, y down from top of screen
        self.window_id1 = self.openterminal(self.working_directory1, 0, 10)
        self.window_id2 = self.openterminal(self.working_directory2, 350, 325)
        self.window_id3 = self.openterminal(self.working_directory3, 700, 650)

    def callback_open_all_terminals(self):
        self.open_all_desired_terminals()


def main():
    root = Tk()
    root.grid_columnconfigure(2, minsize=25)
    root.grid_rowconfigure(2, minsize=15)
    root.grid_rowconfigure(3, minsize=15)
    app = MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    main()
