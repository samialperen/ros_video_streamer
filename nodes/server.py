#!/usr/bin/env python

import rospy

from dynamic_reconfigure.server import Server
from ros_video_streamer.cfg import QTConfig

def callback(config, level):
    rospy.loginfo("""Reconfigure Request: {video_name} """.format(**config))
    return config

if __name__ == "__main__":
    rospy.init_node("dynamic_tutorials", anonymous = False)

    srv = Server(QTConfig, callback)
    rospy.spin()
