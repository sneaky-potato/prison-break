#!/usr/bin/env python
import rospy
from prison.msg import Position
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import os

"""
An template file
You may choose not to follow this template as well
Design your strategy and keep a note of used matches too
Publish the path in the end
"""


class Person():
    def __init__(self, output_path):
        self.pub = rospy.Publisher("/match_light", Position, queue_size=10)
        self.bridge = CvBridge()
        self.output_path = output_path
    
    def person_callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')

        output_image_path = os.path.join(self.output_path, (str(rospy.get_time()) + '.png'))
        rospy.loginfo(rospy.get_caller_id() + " Snap returned")
        cv2.imwrite(output_image_path, cv_image)
                      


def send():

    rospy.init_node('prison_break', anonymous=True)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    output_absolute_path = os.path.abspath(os.path.join(dir_path, os.pardir, os.pardir, 'output'))

    person = Person(output_absolute_path)
    
    rospy.Subscriber("/snap_return", Image, person.person_callback)
    print("Beginning to light up the environment")

    r = rospy.Rate(0.1)
    msg = Position()
    msg.x = 10
    msg.y = 10
  
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        person.pub.publish(msg)
        r.sleep()
  
if __name__ == '__main__':
    send()
