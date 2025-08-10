#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np

class TalkerClass:
    def __init__(self):
       rospy.init_node('talker_node',anonymous=True)
       self.publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
       self.subscriber = rospy.Subscriber("/base_scan", LaserScan, self.callback)
       self.rate = rospy.Rate(10)
       rospy.spin()   
    def callback(self, scan_data):
       ranges= np.array(scan_data.ranges)
       ranges= ranges[(~np.isnan(ranges))&(ranges > 0.0)]
       msg = Twist()
       threshold = 1.0
       front_angle= 50
       total_samples = len(scan_data.ranges)
       mid_index = total_samples // 2
       sector_width= int((front_angle / 220.0) * total_samples)
       front_ranges = scan_data.ranges[mid_index - sector_width:mid_index * sector_width]
       
       valid_front_ranges_gauche = [r for r in ranges[:int(total_samples / 2)] if not np.isnan(r) and r > 0.0]
       valid_front_ranges_droite = [r for r in ranges[int(total_samples / 2):] if not np.isnan(r) and r > 0.0]

       if valid_front_ranges_gauche and min(valid_front_ranges_gauche) < threshold:
          msg.linear.x= 0.2
          msg.angular.z= 0.4
       if valid_front_ranges_droite and min(valid_front_ranges_droite) < threshold:
          msg.linear.x= 0.2
          msg.angular.z= -0.4        
       else:
          msg.linear.x= 0.2
          msg.linear.z= 0.0
       self.publisher.publish(msg)
    
        
if __name__=='__main__':
   try:
      talker= TalkerClass()
   except rospy.ROSInterruptException:
       pass
      