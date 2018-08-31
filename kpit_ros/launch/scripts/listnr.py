#!/usr/bin/env python  
import roslib
roslib.load_manifest('kpit_ros')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')

    listener = tf.TransformListener()

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(4, 2, 0, 'turtle2')

    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0)
    rospy.sleep(1)
    (trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
    (t) = listener.lookupTwist('/turtle2', '/turtle1', rospy.Time(0), rospy.Duration(.01))
    
    distance = math.sqrt(trans[1]*trans[1]+trans[0]*trans[0])
    # print(distance)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
            (t) = listener.lookupTwist('/turtle2', '/turtle1', rospy.Time(0), rospy.Duration(.01))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        euler = tf.transformations.euler_from_quaternion(rot)
        cmd = geometry_msgs.msg.Twist()
        
        # print(distance)  
        angle=  math.atan2(abs(trans[1]), abs(trans[0]))
        distance1 = math.sqrt(trans[1]*trans[1]+trans[0]*trans[0])
        # print(angle)
        temp_d=0
        # if t[1][2]!=0:
        #     rospy.sleep(1)
        flag=0
        linear=4

        if distance>distance1 and trans[0]>0:
            linear=-linear
        if distance<distance1 and trans[0]<0:
            linear=-linear

        
        if abs(distance1-distance)<.35:
            # print("mndkfn")
            linear=0

        elif distance<distance1 and t[1][2]==0:
            linear = linear
            flag=1
            # print("Asfdgfh")            
        elif distance>distance1 and t[1][2]==0:
            linear = linear
            # print("jdhfgsf")

        elif abs(euler[2])>0.05:
            linear = 0
            # print("iuytfd")    

            # print(cmd.linear.x)
        cmd.angular.z = 5*euler[2]+.1
        cmd.linear.x=linear
        turtle_vel.publish(cmd)

        # rospy.sleep() 
        rate.sleep()