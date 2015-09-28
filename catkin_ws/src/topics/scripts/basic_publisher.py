#!/usr/bin/env python

"""Basic ROS publisher example.

This example introduces ROS topics and creates a basic ROS node called
'basic_publisher' that counts how many messages it sends and publishes this
number on '/basic_topic'.

This can be observed by running 'rosnode list' and 'rostopic list'.
"""

import rospy
from std_msgs.msg import Int64


if __name__ == "__main__":
    # Initialize node.
    rospy.init_node("basic_publisher")

    # Create publisher: name the topic, specify the message type and set the
    # size of the outgoing message queue.
    pub = rospy.Publisher("/basic_topic", Int64, queue_size=1)

    # Set the publishing rate in Hz.
    rate = rospy.Rate(1)

    # Maintain count.
    count = 0

    # Run until stopped.
    while not rospy.is_shutdown():
        # Create message.
        msg = Int64(count)

        # Increment count.
        count += 1

        # Publish message.
        pub.publish(msg)

        # Wait until it's time to publish again.
        rate.sleep()
