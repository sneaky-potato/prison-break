#!/usr/bin/env python
import rospy
from prison.msg import Position
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np


RADIUS = 10

class Prison():
      def __init__(self, img):
            self.map = img
            self.radius = RADIUS
            self.bridge = CvBridge()
            self.pub = rospy.Publisher("/snap_return", Image, queue_size = 100)

      def match_light_callback(prison, data):
            data.x = int(data.x)
            data.y = int(data.y)
            print(prison.map.shape)
            height, width, channels = prison.map.shape
            print("Recieved coordinates:", data.x, data.y)
            if(data.x < 0 or data.y < 0 or data.x >= height or data.y >= width):
                  rospy.loginfo(rospy.get_caller_id() + " Forbidden action [COORDINATES INVALID]")
            else:  
                  newimg = cv2.cvtColor(prison.map, cv2.COLOR_BGR2GRAY)
                  black = np.zeros(prison.map.shape,dtype=np.uint8)
                  if newimg[data.x][data.y] <= 20:
                        rospy.loginfo(rospy.get_caller_id() + " Forbidden action [COORDINATES INVALID]")
                        image_message = prison.bridge.cv2_to_imgmsg(black, encoding="passthrough")
                        prison.pub.publish(image_message)
                  elif newimg[data.x][data.y] >= 230:
                        cv2.circle(black,(data.y,data.x),prison.radius, (255, 255, 255), thickness=cv2.FILLED)
                        black=cv2.cvtColor(black, cv2.COLOR_BGR2GRAY)
                        # patch_image = image
                        cv_image = cv2.cvtColor(cv2.bitwise_and(newimg, black),cv2.COLOR_GRAY2BGR)
                        cv_image = cv_image[data.x - RADIUS // 2 : data.x + RADIUS // 2, data.y - RADIUS // 2 : data.y + RADIUS // 2]
                        image_message = prison.bridge.cv2_to_imgmsg(cv_image, encoding="passthrough")
                        prison.pub.publish(image_message)
                  else:
                        rospy.loginfo(rospy.get_caller_id() + "Forbidden action [MAP INVALID]")


def listener():

      rospy.init_node('prison', anonymous=True)
      img = cv2.imread('../../map/maze.png')

      prison = Prison(img)

      rospy.Subscriber("/match_light", Position, prison.match_light_callback)
      print("Switched off the lights, game begins")

      rospy.spin()
  
if __name__ == '__main__':
      listener()
