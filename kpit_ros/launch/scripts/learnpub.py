#!/usr/bin/env python

"""Script to move turtle bot according to requirement"""

import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897


def circle_move(speed, angle, clockwise):
    """For moving the turtle in circle"""
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher(
        'turtle1/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    # We wont use linear components
    vel_msg.linear.x = 1.5
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    time0 = rospy.Time.now().to_sec()
    current_angle = 0

    while current_angle < relative_angle:
        velocity_publisher.publish(vel_msg)
        time1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(time1-time0)

    # Forcing our robot to stop
    vel_msg.angular.z = 0
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
    return


def move_straight(speed, distance, iis_forward):
    """Move the turtle bot in straight line"""
    # Starts a new node

    velocity_publisher = rospy.Publisher(
        'turtle1/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Checking if the movement is forward or backwards
    if iis_forward:
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    # Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        # Setting the current time for distance calculus
        time0 = rospy.Time.now().to_sec()
        current_distance = 0

        # Loop to move the turtle in an specified distance
        while current_distance < distance:
            # Publish the velocity
            velocity_publisher.publish(vel_msg)
            # Takes actual time to velocity calculus
            time1 = rospy.Time.now().to_sec()
            # Calculates distancePoseStamped
            current_distance = speed*(time1-time0)
        # After the loop, stops the robot
        vel_msg.linear.x = 0
        # Force the robot to stop
        velocity_publisher.publish(vel_msg)
        return


if __name__ == '__main__':
    rospy.init_node('robot_cleaner', anonymous=True)
    rospy.Rate(100.0)
    circle_move(60, 377, True)
    move_straight(1.5, 4, True)
    circle_move(60, 350, True)
