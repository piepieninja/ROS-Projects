#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "yo, dat data is: %s", data)
    x_dot = data.linear.x
    y_dot = data.linear.y
    theta = data.angular.z
    rospy.loginfo("x vel:" + str(x_dot) + ", y vel: " + str(y_dot) + ", theta: " + str(theta))
    # derived from these slides in class: https://uga.view.usg.edu/d2l/le/content/1627420/viewContent/24268161/View
    # the project required the following constrains:
    b = 100/2 # b, defined as 100cm, is half the distance from one wheel to another
    r = 5     # r was defined a 5cm 
    # now we calcuate the phi_x and phi_y
    # the full form is written for clarity
    phi_r = (x_dot/r) + 0*y_dot + ((b*theta)/r)
    phi_l = (x_dot/r) + 0*y_dot - ((b*theta)/r)
    rospy.loginfo("phi_r: " + str(phi_r) + " | " + "phi_l" + str(phi_l))
    pub = rospy.Publisher('DIFFERENTIAL_INVERSE_KINEMATICS_OUTPUT', String, queue_size=10)
    wheel_vel_msg = String()
    wheel_vel_msg = "phi_r" + str(phi_r) + "\n"
    wheel_vel_msg = "phi_l" + str(phi_l)
    pub.publish(wheel_vel_msg)

    
def listener():
    rospy.init_node('Listen_Turtle', anonymous=True)    
    rospy.Subscriber("cmd_vel_mux/input/navi", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
