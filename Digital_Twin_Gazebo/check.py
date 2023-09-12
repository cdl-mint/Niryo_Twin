#!/usr/bin/env python
import sys
import rospy
import moveit_commander

def list_planning_groups():
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    planning_groups = robot.get_group_names()
    moveit_commander.roscpp_shutdown()
    return planning_groups

if __name__ == '__main__':
    rospy.init_node('list_planning_groups', anonymous=True)

    try:
        planning_groups = list_planning_groups()
        print("Available planning groups:")
        print(planning_groups)
    except rospy.ROSInterruptException:
        print("Program interrupted")

