from pyniryo import *

# -- IP address of Niryo Robot --
robot1_ip = "192.168.0.101"
robot2_ip = "192.168.0.103"

# Ipaddress of Niryo Robot
robot1 = NiryoRobot(robot1_ip)
robot2 = NiryoRobot(robot2_ip)

# -- Calibrating Robots
robot1.calibrate_auto()
robot2.calibrate_auto()

# -- updating tool
robot1.update_tool()
robot2.update_tool()

# pickup robot1
robot1_pick_pose = [0.643, -0.369, -0.328, -0.021, -0.858, -0.017]
robot1_give_pose = [1.5, 0.191, -0.164, 0.16, 0.04, 0]
robot2_give_pose = [1.5, 0.191, -0.164, 0.16, 0.04, 0]
robot2_place_pose = [-0.643, -0.369, -0.328, -0.021, -0.858, -0.017]

while True:
    robot1.open_gripper()
    robot1.move_joints(robot1_pick_pose)
    robot1.close_gripper()
    
    robot2.give_pose(robot2_give_pose)
    robot2.open_gripper()
    
    robot1.move_joints(robot1_give_pose)
    robot2.close_gripper()
    robot1.open_gripper()
    
    robot1.move_joints(robot1_pick_pose)
    
    robot2.move_joints(robot2_place_pose)
    robot2.open_gripper()
    break

    
    
########## testing code ##########
# Initializing ROS node
"""
rospy.init_node('niryo_ned_example_python_ros_wrapper')

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
"""