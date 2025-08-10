#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class TalkerClass:
    def __init__(self):
       self.topic= "/talker"
       self.publisher = rospy.Publisher(self.topic, String, queue_size=10)
       rospy.init_node('talker_node',anonymous=True, log_level=rospy.DEBUG)
       self.rate = rospy.Rate(10)
       
    def talk(self):
       
        messages = String()
        while not rospy.is_shutdown():
            
            messages.data = " Hello"
            
            rospy.loginfo(messages)
            rospy.logwarn("this is a warning")
            rospy.logerr("this is a error")
            rospy.logdebug("this is a debug message")
            self.publisher.publish(messages)
            self.rate.sleep()
          
          
    #def name(self):
     #   self._
        
if __name__=='__main__':
   try:
      talker= TalkerClass()
      talker.talk()
   except rospy.ROSInterruptException:
       pass
      