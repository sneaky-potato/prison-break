#!/usr/bin/env python
import rospy
from prison.msg import Position
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import os


RADIUS = 10

class Prison():
      def __init__(self, img):
            self.map = img
            self.radius = RADIUS
            self.bridge = CvBridge()
            self.pub = rospy.Publisher("/snap_return", Image, queue_size = 100)

      def match_light_callback(self, data):
            data.x = int(data.x)
            data.y = int(data.y)
            print(self.map.shape)
            height, width, channels = self.map.shape

            print("Recieved coordinates:", data.x, data.y)
            if(data.x < 0 or data.y < 0 or data.x >= height or data.y >= width):
                  rospy.loginfo(rospy.get_caller_id() + " Forbidden action [COORDINATES INVALID]")
            else:  
                  newimg = cv2.cvtColor(self.map, cv2.COLOR_BGR2GRAY)
                  black = np.zeros(newimg.shape,dtype=np.uint8)

                  if newimg[data.x][data.y] <= 20:
                        rospy.loginfo(rospy.get_caller_id() + " Forbidden action [COORDINATES INVALID]")
                        image_message = self.bridge.cv2_to_imgmsg(black, encoding="passthrough")
                        self.pub.publish(image_message)

                  elif newimg[data.x][data.y] >= 230:
                        cv2.circle(black,(data.y,data.x),self.radius, (255, 255, 255), thickness=cv2.FILLED)

                        cv_image = cv2.cvtColor(cv2.bitwise_and(newimg, black),cv2.COLOR_GRAY2BGR)
                        cv_image = cv_image[data.x - RADIUS: data.x + RADIUS, data.y - RADIUS: data.y + RADIUS]
                        image_message = self.bridge.cv2_to_imgmsg(cv_image, encoding="passthrough")
                        self.pub.publish(image_message)
                        rospy.loginfo(rospy.get_caller_id() + "Snap published")

                  else:
                        rospy.loginfo(rospy.get_caller_id() + "Forbidden action [MAP INVALID]")


def listener():

      rospy.init_node('prison', anonymous=True)

      dir_path = os.path.dirname(os.path.realpath(__file__))
      absolute_path = os.path.abspath(os.path.join(dir_path, os.pardir, os.pardir, 'map', 'maze.png'))

      print("Map path =", absolute_path)

      img = cv2.imread(absolute_path)

      try:
            print("Map configured =", img.shape)
      except:
            print("Reconfigure map [NOT FOUND]")
            exit()

      prison = Prison(img)

      rospy.Subscriber("/match_light", Position, prison.match_light_callback)
      print("Switched off the lights, game begins")

      rospy.spin()
  
if __name__ == '__main__':
      listener()
