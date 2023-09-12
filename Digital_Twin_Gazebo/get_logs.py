#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
import datetime

last_time = None
previous_positions = None

def joint_states_callback(msg):
    global last_time, previous_positions
    # Get the positions of joint_1 to joint_6
    positions = dict(zip(msg.name, msg.position))
    joint_1_pos = positions['joint_1']
    joint_2_pos = positions['joint_2']
    joint_3_pos = positions['joint_3']
    joint_4_pos = positions['joint_4']
    joint_5_pos = positions['joint_5']
    joint_6_pos = positions['joint_6']

    # Check if there are changes in any one of the joints
    if previous_positions is None or \
       joint_1_pos != previous_positions[0] or \
       joint_2_pos != previous_positions[1] or \
       joint_3_pos != previous_positions[2] or \
       joint_4_pos != previous_positions[3] or \
       joint_5_pos != previous_positions[4] or \
       joint_6_pos != previous_positions[5]:
        
        # Print the joint positions as a list with three decimal precision
        print("[{:.3f}, {:.3f}, {:.3f}, {:.3f}, {:.3f}, {:.3f}]".format(
            joint_1_pos, joint_2_pos, joint_3_pos, joint_4_pos, joint_5_pos, joint_6_pos))
        
        # Save the joint positions to the file
        with open("scenario_4.txt", "a") as file:
            file.write("[{:.3f}, {:.3f}, {:.3f}, {:.3f}, {:.3f}, {:.3f}]\n".format(
                joint_1_pos, joint_2_pos, joint_3_pos, joint_4_pos, joint_5_pos, joint_6_pos))
        
        last_time = datetime.datetime.now()
        previous_positions = (joint_1_pos, joint_2_pos, joint_3_pos, joint_4_pos, joint_5_pos, joint_6_pos)

def main():
    rospy.init_node('joint_states_listener', anonymous=True)
    rospy.Subscriber("/joint_states", JointState, joint_states_callback)
    rate = rospy.Rate(30)  # 60Hz

    try:
        while not rospy.is_shutdown():
            rospy.spin()
            rate.sleep()
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == '__main__':
    main()
