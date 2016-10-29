#!/usr/bin/env python

"""Basic ROS node example.

This creates a basic ROS node called 'basic_node' that persists until ROS is
stopped.

This can be observed by running 'rosnode list'.
"""

import rospy


if __name__ == "__main__":
    # Initialize node
    rospy.init_node("basic_node")

    # Run until stopped
    rospy.spin()
