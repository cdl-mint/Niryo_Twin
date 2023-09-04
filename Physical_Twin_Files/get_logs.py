from niryo_robot_python_ros_wrapper.ros_wrapper import *
import sys
import rospy
import time
from datetime import datetime
import argparse
import os


# Parsing command line arguments for scenario and iteration
parser = argparse.ArgumentParser(description='Choose a scenario and iteration for the robot movement.')
parser.add_argument('scenario', type=int, choices=range(1, 6),
                    help='an integer for the scenario (1-5)')
parser.add_argument('iteration', type=int, help='an integer for the iteration')
args = parser.parse_args()
scenario = args.scenario
iteration = args.iteration



rospy.init_node('niryo_blockly_interpreted_code2')
n = NiryoRosWrapper()
rospy.timer.Rate(30)

prev_pos_list = n.get_joints()
tolerance = 0.01  # Adjust this value as needed
t1 = datetime.now()

def is_moved(current, previous, tolerance):
    return any(abs(c - p) > tolerance for c, p in zip(current, previous))

log_file = "scenario_{scenario}_iteration_{iteration}.txt".format(scenario=scenario, iteration=iteration)

if os.path.exists(log_file):
    os.remove(log_file)
    print('Existing file is deleted')
else:
    pass

try:
    while not rospy.is_shutdown():
        while True:
            rospy.sleep(0.06)
            current_pos_list = [round(num, 4) for num in n.get_joints()]
            if is_moved(current_pos_list, prev_pos_list, tolerance):  # Checking if position has changed
                t2 = datetime.now()
                log_line = str(current_pos_list) + ', ' + str((t2 - t1).microseconds/1000) + '\n'  # prepare line to be logged
                t1 = t2
                with open(log_file, 'a') as file:  # Change 'w' to 'a' for append mode
                    file.write(log_line)  # write the log line to file
                print(log_line)
                prev_pos_list = current_pos_list  # Updating the previous position

        print('Logs written to ' + log_file)

except KeyboardInterrupt:
    print('Keyboard interrupt detected, exiting...')
    print(rospy.is_shutdown())
    sys.exit()
