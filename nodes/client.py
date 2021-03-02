#!/usr/bin/env python

import rospy
import dynamic_reconfigure.client

import cv2
import sys

def callback(config):
    rospy.loginfo("Config set to {video_name} ".format(**config))
    video_name = config["video_name"]

    cap = cv2.VideoCapture(video_name)
    if not cap.isOpened():
        print "Error opening resource: " + str(video_name)
        print "Maybe opencv VideoCapture can't open it"
        sys.exit(0)
	
    print "Correctly opened resource, starting to show feed."
    rval, frame = cap.read()
    while rval:
	    cv2.imshow("Stream: " + video_name, frame)
	    rval, frame = cap.read()
	    key = cv2.waitKey(20)
	    # print "key pressed: " + str(key)
	    # exit on ESC, you may want to uncomment the print to know which key is ESC for you
	    if key == 27 or key == 1048603:
	    	break
    cv2.destroyWindow("preview")

if __name__ == "__main__":
    rospy.init_node("dynamic_client")
    
    video_name = "default_video.mp4"
    
    cap = cv2.VideoCapture(video_name)
    if not cap.isOpened():
        print "Error opening resource: " + str(video_name)
        print "Maybe opencv VideoCapture can't open it"
        sys.exit(0)
	
    print "Correctly opened resource, starting to show feed."
    rval, frame = cap.read()
    while rval:
	    cv2.imshow("Stream: " + video_name, frame)
	    rval, frame = cap.read()
	    key = cv2.waitKey(20)
	    # print "key pressed: " + str(key)
	    # exit on ESC, you may want to uncomment the print to know which key is ESC for you
	    if key == 27 or key == 1048603:
	    	break
    	elif:
    	    client = dynamic_reconfigure.client.Client("dynamic_tutorials", timeout=30, config_callback=callback)
            rospy.wait_for_service("/dynamic_tutorials/set_parameters")

    client = dynamic_reconfigure.client.Client("dynamic_tutorials", timeout=30, config_callback=callback)


    r = rospy.Rate(30)
    rospy.spin()







