from pyniryo import *


# Robot IP's
robot1_ip = "192.168.0.101"
robot2_ip = "192.168.0.108"

# Robot Initialisatios
robot1 = NiryoRobot(robot1_ip)
robot2 = NiryoRobot(robot2_ip)

# Robot Calibrations
robot1.calibrate_auto()
robot2.calibrate_auto()

# Robot Tool Updates
robot1.update_tool()
robot2.update_tool()

def homing_robots():
    robot1.move_joints(robot_home)
    robot2.move_joints(robot_home)

def obj_exchange():
    robot1.move_joints(robot1_pick_pose)
    robot1.close_gripper()
    robot1.move_joints(exchange_pose1)
    robot2.move_joints(exchange_pose2)
    robot1.move_joints(about_to_exchange1)
    robot2.move_joints(about_to_exchange2)
    robot2.close_gripper()
    robot1.open_gripper()
    robot2.move_joints(robot2_place_pose)
    robot1.move_joints(robot_home)
    robot2.open_gripper()
    robot2.move_joints(robot_home)
    return True


# Predefined Positions
robot_home = [0,0,0,0,0,0]

robot1_pick_pose = [0.643, -0.40, -0.328, -0.021, -0.858, -1.0]
robot2_place_pose = [-0.643, -0.369, -0.328, -0.021, -0.858, -0.017]

exchange_pose1 = [-1.65, 0.191, -0.164, -1.6, 0.04, 0]
exchange_pose2 = [1.65, 0.15, -0.164, 0.0, 0.04, 0]

about_to_exchange1 = [-1.65, 0.08, -0.05, -1.6, 0.04, 0]
about_to_exchange2 = [1.65, 0.08, -0.10, 0.0, 0.04, 0]

# Unused positions
robot1_give_pose = [1.5, 0.191, -0.164, 0.16, 0.04, 0]
robot2_give_pose = [1.5, 0.191, -0.164, 0.16, 0.04, 0]


try:
    homing_robots()
    obj_exchange()
finally:
    robot1.close_connection()
    robot2.close_connection()
