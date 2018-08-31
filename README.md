## Overview

This includes Moving turtle using puthon script in circular and straight line, 
one bot mimic the moment of other bot.
Also an ROS package to control the bot in Gazebo, having some plugins, Sensors
like lazer, camera and the simulation can be seen in Rviz

===================================================================================

### How to build:

first create two package in ros name kpit_ros and my_teleop in ~/catkin_ws/src 
directory using below command
	
	:~/catkin_ws/src$ catkin_create_pkg kpit_ros
	:~/catkin_ws/src$ catkin_create_pkg my_teleop
	
Download the package and extract in ~/catkin_ws/src and replace both with packages
that we created above with these.
Now, do a catkin_make in catkin workspace


Ros, gazebo, Rviz and teleop can be launch using below command
	$ roslaunch kpit_ros zg.launch 

Using the same terminal you can now teleop your bot.


### How to use teleop:  
		_________________________________  
		|								|  
		|	Reading from keyboard 		|  
		|	--------------------------- |  
		|	Use 'WS' to forward/back    |  
		|	Use 'AD' to left/right      |  
		|	Use 'Q' to stop             |  
		|_______________________________|  

Also a seperate teleop can be launched using 
	$rosrun my_teleop teleop_keyboard 

For point cloud : 

	$roslaunch kpit_ros assembler.launch 
	$rosrun kpit_ros laser_assembler_service_caller 

======================================================================================


Controling the bot using python script and aslo the mimic using below commands
	$ roslaunch kpit_ros SwatchBharat.launch     //For python script
	$ roslaunch kpit_ros tf_lisnr.launch 		 //For mimic

======================================================================================


