#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import cv2

video_name = ""

def callback(data):
    global video_name
    video_name = data.data
    return
   
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('video_streamer', anonymous=True)

    rospy.Subscriber("video_name", String, callback)

    
    global video_name
    prev_name = ""
    
    
    rate = rospy.Rate(100)
    
    
    
    #if not cap.isOpened():
    #    print("Error opening resource: " + str(video_name))
    #    print("Maybe opencv VideoCapture can't open it")
    #    sys.exit(0)
	
	# Open the video stream.
    cap = cv2.VideoCapture(video_name)
    
    while not rospy.is_shutdown():

	    
	    # Check was video_name changed?
        if video_name != prev_name:
	        cap.open(video_name)
	        prev_name = video_name
        else:
            rate.sleep()
        
        while(cap.isOpened()):
            if video_name != prev_name:
	            break        
            ret, frame = cap.read()
            if ret:
                cv2.imshow('frame',frame)
                
            else:
                print("Loop")
                cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            
    	    key = cv2.waitKey(100)    
            if key == 27 or key == 1048603:
                cv2.destroyWindow("preview")
                rospy.signal_shutdown("Program closed dude")
                exit(0)

            
	  
if __name__ == '__main__':
    listener()
