#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class Move_Turtle():
    def __init__(self):
        rospy.init_node('Move_Turtle', anonymous=False)
        rospy.on_shutdown(self.shutdown)        
        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
        print 'yo Im gunna move'
        r = rospy.Rate(10);
        move_cmd = Twist()
        move_cmd.linear.x = 0.2
        move_cmd.linear.y = 0.0
        move_cmd.linear.z = 0.0
        move_cmd.angular.x = 0.0
        move_cmd.angular.y = 0.0
        move_cmd.angular.z = 0.0
        while not rospy.is_shutdown():
            self.cmd_vel.publish(move_cmd)
            r.sleep()
            
    def shutdown(self):
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)
        
if __name__ == '__main__':
    try:
        Move_Turtle()
    except:
        print 'we done here boiz'
