#!/usr/bin/env python
import rospy
from prison.msg import Position
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

def send():

    rospy.init_node('prison_break', anonymous=True)
    pub = rospy.Publisher("/match_light", Position)

    r = rospy.Rate(10) #10hz
    msg = Position()
    msg.x = -4.5
    msg.y = 7.9
  
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()
  
if __name__ == '__main__':
      send()
