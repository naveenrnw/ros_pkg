cmake_minimum_required(VERSION 2.8.3)
project(kpit_ros)
set(CMAKE_BUILD_TYPE Debug)

find_package(cmake_modules REQUIRED)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  tf
  laser_geometry
)
find_package(PCL 1.6 REQUIRED COMPONENTS common apps)

catkin_package()

include_directories(${PCL_INCLUDE_DIRS} ${EIGEN_INCLUDE_DIRS} ${catkin_INCLUDE_DIRS} ${PROJECT_SOURCE_DIR}/include)




MESSAGE("######################################################################PCL#####################################################################")
MESSAGE("PCL_FOUND:" ${PCL_FOUND})
MESSAGE("PCL_INCLUDE_DIRS:" ${PCL_LIBRARY_DIRS})
MESSAGE("PCL_LIBRARIES:" ${PCL_LIBRARIES})
MESSAGE("PCL_LIBRARY_DIRS:" ${PCL_LIBRARY_DIRS})
MESSAGE("PCL_VERSION:" ${PCL_VERSION})
MESSAGE("PCL_COMPONENTS:" ${PCL_COMPONENTS})
MESSAGE("PCL_DEFINITIONS:" ${PCL_DEFINITIONS})


MESSAGE("######################################################################catkin#####################################################################")
MESSAGE("catkin_LIBRARIES: " ${catkin_LIBRARIES})



add_executable(laser_scan_to_pointcloud src/laser_scan_to_pointcloud.cpp )
target_link_libraries(laser_scan_to_pointcloud  ${catkin_LIBRARIES}  ${PCL_LIBRARIES}  )


add_executable(laser_assembler_service_caller src/laser_assembler_service_caller.cpp )
target_link_libraries(laser_assembler_service_caller  ${catkin_LIBRARIES}  ${PCL_LIBRARIES}  )

add_executable(temp1 src/temp1.cpp )
target_link_libraries(temp1 ${catkin_LIBRARIES} ${PCL_LIBRARIES} )
