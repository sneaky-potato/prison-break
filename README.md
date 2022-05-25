# Prison-Break &middot;

>Trapped within a dark labyrinth with nothing but a matchbox in my left pocket, a fistful supply of sticks inside it, unbeknown to the future ahead, I kept wondering about what led to this unfortunate event.

Repository for the task round of ARK fresher selections 2022

Please make sure you've read and understood the problem statement before tinkering.

## Rules

- Start from the starting position on the maze

- You are not allowed to use the global origin information for solving task

- You can only make your next move using the information from the snapshot returned and nothing else

- You are not allowed to light up an area which does not lie in the vicinity of your current / visited location

## Installing / Getting started

A quick introduction of the minimal setup you need to get the package compiled and ready for the task

```shell
cd ~/catkin_ws/src
git clone https://github.com/sneaky-potato/prison-break.git prison
catkin clean -y
catkin build prison
```

If you run into build issues, make sure the name of the package is consistent everywhere i.e. ```CMakeLists.txt```, ```package.xml``` and directory name (supposed to be **prison**)

## Scripts

You will find 2 python files (ROS nodes) inside the ```src/scripts``` directory-

- ```main.py```
- ```prison-break.py```

You are supposed to write your solution by taking ```prison-break.py``` as a reference.

You may also choose to follow your own design, ```prison-break.py``` is only provided as a reference.

## Msg reference

There are 2 msg files being used-

- [Position](https://github.com/sneaky-potato/prison-break/blob/master/msg/Position.msg)

```shell
float64 x
float64 y
```

Note: ```Postion.x``` is measured against the vertical axis and ```Position.y``` against the horizontal axis

- [Image](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)

```shell
ROS Image message provided under sensor_msgs
```

## Topic Reference

There are mainly 2 topics used for communicating data-

- /match_light

>Publish your coordinates ([Position.msg](https://github.com/sneaky-potato/prison-break/blob/master/msg/Position.msg)) to this topic

- /snap_return

>Subscribe to this topic to get a snapshot of the image ([Image.msg](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html))

## Running the server

```shell
roscore
```

```shell
cd ~/catkin_ws
chmod +x src/prison-break/src/scripts/main.py
source devel/setup.bash
rosrun prison main.py
```
