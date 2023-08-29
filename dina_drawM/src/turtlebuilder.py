#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pi

rospy.init_node('robot_cleaner', anonymous=True)
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()

def move(distance,vel):
        vel_msg.linear.x = vel
    
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

            
        while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            
            t1=rospy.Time.now().to_sec()
            
            current_distance= vel*(t1-t0)
            
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
    

def rotation(angle):
        vel_msg.linear.x = 0
        vel_msg.angular.z = pi*angle/180

        velocity_publisher.publish(vel_msg)
        rospy.sleep(1)

        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

# -90 for right and 90 for left

if __name__ == '__main__':
    rospy.sleep(1)
    try:
        #diangle
        rotation(45)
        move(4,4)
        #down
        rotation(-135)
        move(4,2)
        #left dent
        rotation(-90)
        move(.50,2)

        #down I
        rotation(90)
        #move(.7,1)
        move(.75,1)

        #move right
        rotation(90)
        move(1.5,2)

        #move back up
        rotation(90)
        move(.75,1)

        #move left dent again
        rotation(90)
        move(.5,2)

        # move up
        rotation(-90)
        move(4,4)

        # move right
        rotation(-90)
        move(.40,2)

        # back up
        rotation(90)
        move(.9,1)

        # move left
        rotation(90)
        move(1,1)
        
        #second /
        rotation(45)
        move(4.5,4)

        #first \
        rotation(-95)
        move(3.9,4)

        rotation(50)
        move(1,1)

        rotation(90)
        move(.7,1)

        rotation(90)
        move(.4,2)

        rotation(-90)
        move(4,4)

        rotation(-90)
        move(.6,2)

        rotation(90)
        move(.75,1)

        rotation(90)
        move(1.5,2)

        rotation(90)
        move(.75,1)

        rotation(90)
        move(.55,2)

        rotation(-90)
        move(4,2)

        rotation(-140)
        move(4,4)

    except rospy.ROSInterruptException: pass