# ros_video_streamer

This package allows users to open video files in opencv image window. It uses ```dynamic_reconfiguration```, so one can dynamically change parameters on runtime. 

For example, under cfg directory, dynamic parameters were defined. Right now, there is only one parameter called ```video_name```. User can change video name via ROS services.


## Usage
* Run roscore
```
$ roscore
```
* Run Dynamic Reconfiguration Server
```
$ rosrun ros_video_streamer server.py
```
* Run Dynamic Reconfiguration Client 
```
$ rosrun ros_video_streamer client.py
```
* Set name of the video (give full path)
```
$ rosrun dynamic_reconfigure dynparam set dynamic_tutorials video_name /home/user/path_to_video/video_name.mp4
```
* What dynamic reconfigure dynparam set does is to send commands to the service dynamic_tutorials/set_parameters.


**TODO:** Right now, if you set another video name, while one video is playing, you can not see it directly, unless you enter ESC. 
