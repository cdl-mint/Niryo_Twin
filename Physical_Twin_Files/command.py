#!/usr/bin/env python
import sys
import rospy
import moveit_commander
import trajectory_msgs.msg

def move_robot(move_group, joint_positions):
    move_group.set_joint_value_target(joint_positions)
    plan = move_group.go(wait=True)
    return plan

def main():
    rospy.init_node('rviz_robot_controller', anonymous=True)

    # Initialize MoveIt! commander
    moveit_commander.roscpp_initialize(sys.argv)

    # Create a MoveGroupCommander for the robot planning group
    move_group = moveit_commander.MoveGroupCommander("arm")

    # Set the planner and other planning parameters (if needed)
    # move_group.set_planner_id("RRTConnectkConfigDefault")

    # Set the planning tolerance (optional)
    # move_group.set_goal_joint_tolerance(0.01)
    # Set the planning speed (20% of the maximum speed)
    move_group.set_max_velocity_scaling_factor(0.2)

    try:
        # Define the target joint positions (use your desired values in radians)
        target_positions_list = [
            [0, 0, 0, 0, 0, 0],
            [2.5, 0.5, 0.5, 1.8, -1.5, 0.0],
            [-1.3, -0.5, -0.2, 0.0,-0.750, 2.3],
            [-1.0, 0.20, -1.2, -0.0, 1.0, 2.3],
            [0.3, 0.20, 1.2, 1.9, -1.4, 0.0],
            [2.0,-0.3, 0.5, -1.75, -1.3, 1.0],
            [0, 0, 0, 0, 0, 0]
            ]


        # Move the robot to each target joint position
        for i, target_joint_positions in enumerate(target_positions_list):
            print("Moving to Target {}".format(i + 1))
            move_robot(move_group, target_joint_positions)

    except rospy.ROSInterruptException:
        print("Program interrupted")

    finally:
        # Shut down MoveIt! commander
        moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    main()
