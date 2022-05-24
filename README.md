# Prison-Break &middot;

> Repository for the task round of ARK fresher selections 2022

Please make sure you've read and understood the problem statement before tinkering

## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

```shell
cd ~/catkin_ws/src
git clone https://github.com/sneaky-potato/prison-break.git
catkin clean -y
catkin build prison-break
```

Above commands should get you read by compiling and building the package

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

- [Image](http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html)

```shell
ROS Image message provided under sensor_msgs
```

## Topic Reference

There are mainly 2 topics used for communicating data-

- /match_light

>Publish your coordinates (in [Position.msg](https://github.com/sneaky-potato/prison-break/blob/master/msg/Position.msg)) to this topic

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
rosrun prison-break main.py
```
