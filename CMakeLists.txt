cmake_minimum_required(VERSION 2.8.3)
project(ros_video_streamer)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  roscpp
  rospy
  cv_bridge
)



find_package(OpenCV)


#add dynamic reconfigure api
#find_package(catkin REQUIRED dynamic_reconfigure)
generate_dynamic_reconfigure_options(
  cfg/QT.cfg
  #...
)



catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS})





catkin_install_python(PROGRAMS nodes/server.py nodes/client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)



