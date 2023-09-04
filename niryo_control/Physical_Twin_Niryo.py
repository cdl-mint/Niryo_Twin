from niryo_robot_python_ros_wrapper import *
import rospy
import argparse


# Initializing ROS node
rospy.init_node('niryo_ned_example_python_ros_wrapper')

# set ip of robot
n = NiryoRosWrapper()

conveyor1 = n.set_conveyor()
conveyor2 = n.set_conveyor()

def run_conveyor(robot, conveyor):
    robot.control_conveyor(conveyor, bool_control_on=True,
                           speed=50, direction=ConveyorDirection.FORWARD)

# -- Setting variables
sensor_pin_id = PinID.GPIO_1A

catch_nb = 5

# The pick pose
pick_pose = [1.5, -0.8., 0, 0, -0.7, 0]
# The Place pose
pick_pose = [-1.5, -0.8., 0, 0, -0.7, 0]

# -- MAIN PROGRAM
niryo_robot = NiryoRosWrapper()
niryo_robot.set_arm_max_velocity(20)
niryo_robot.update_tool()

# Activating connexion with conveyor
conveyor_id = niryo_robot.set_conveyor()

for i in range(catch_nb):
    run_conveyor(niryo_robot, conveyor_id)
    while niryo_robot.digital_read(sensor_pin_id) == PinState.LOW:
        niryo_robot.wait(0.1)

    # Stopping robot motor
    niryo_robot.control_conveyor(conveyor_id, True, 0, ConveyorDirection.FORWARD)
    # Making a pick & place
    niryo_robot.pick_and_place(pick_pose, place_pose)

# Deactivating connexion with conveyor
niryo_robot.unset_conveyor(conveyor_id)

