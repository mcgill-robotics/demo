#!/usr/bin/env python

"""Basic ROS subscriber example.

This example creates a basic ROS node called 'basic_subscriber' that subscriber
to the '/basic_topic' topic and prints all the messages it receives to screen.

The publisher-subscriber model can be visualized by running:

    rosrun rqt_graph rqt_graph
"""

import rospy
from std_msgs.msg import Int64


def basic_callback(msg):
    """This function is called whenever a message is received.

    Args:
        msg: Message received.
    """
    print(msg.data)


if __name__ == "__main__":
    # Initialize node.
    rospy.init_node("basic_subscriber")

    # Create subscriber: specify the topic, specify the message type, set the
    # callback and set the size of the incoming message queue.
    pub = rospy.Subscriber("/basic_topic", Int64, basic_callback, queue_size=1)

    # Run until stopped.
    rospy.spin()
