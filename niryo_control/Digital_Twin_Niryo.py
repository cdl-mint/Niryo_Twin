from controller import Robot
import inspect
from controller import Motor, Brake, PositionSensor
import datetime

robot = Robot()
# Getting devices
m1 = robot.getDevice('joint_1')
m2 = robot.getDevice('joint_2')
m3 = robot.getDevice('joint_3')
m4 = robot.getDevice('joint_4')
m5 = robot.getDevice('joint_5')
m6 = robot.getDevice('joint_6')  

# Setting the motor velocity and initial position
m1.setPosition(0)
m2.setPosition(0)
m3.setPosition(0)
m4.setPosition(0)
m5.setPosition(0)
m6.setPosition(0)
    
m1.setVelocity(0)
m2.setVelocity(0)
m3.setVelocity(0)
m4.setVelocity(0)
m5.setVelocity(0)
m6.setVelocity(0)

# Getting the position sensor 
m1_pos = robot.getDevice('joint_1_sensor')
m2_pos = robot.getDevice('joint_2_sensor')
m3_pos = robot.getDevice('joint_3_sensor')
m4_pos = robot.getDevice('joint_4_sensor')
m5_pos = robot.getDevice('joint_5_sensor')
m6_pos = robot.getDevice('joint_6_sensor')

timestep = 64

m1_pos.enable(timestep)
m2_pos.enable(timestep)
m3_pos.enable(timestep)
m4_pos.enable(timestep)
m5_pos.enable(timestep)
m6_pos.enable(timestep)

def run_robot():
    pick_pose = [1.5, -0.8., 0, 0, -0.7, 0]
    place_pose = [-1.5, -0.8., 0, 0, -0.7, 0]

    for i in range(10):
        move_to_position(pick_pose)
        move_to_position(place_pose)

def move_to_position(lis):
    t1 = datetime.datetime.now()
    a1, a2, a3, a4, a5, a6 = lis
    m1.setPosition(a1)
    m2.setPosition(-a2)
    m3.setPosition(a3)
    m4.setPosition(a4)
    m5.setPosition(a5)
    m6.setPosition(a6)
    while robot.step(timestep) != -1: 
        position = [m1_pos.getValue(), 
                    -m2_pos.getValue(), 
                    m3_pos.getValue(),
                    m4_pos.getValue(),
                    m5_pos.getValue(),
                    m6_pos.getValue()]
        m1.setVelocity(0.45)
        m2.setVelocity(0.45)
        m3.setVelocity(0.45)
        m4.setVelocity(0.45)
        m5.setVelocity(0.45)
        m6.setVelocity(0.45)
        if (m1_pos.getValue() <= a1 + 0.01 and m1_pos.getValue() >= a1 - 0.01) and (m2_pos.getValue() <= -a2 + 0.01 and m2_pos.getValue() >= -a2 - 0.01) and (m3_pos.getValue() <= a3 + 0.01 and m3_pos.getValue() >= a3 - 0.01) and (m4_pos.getValue() <= a4 + 0.01 and m4_pos.getValue() >= a4 - 0.01) and (m5_pos.getValue() <= a5 + 0.01 and m5_pos.getValue() >= a5 - 0.01) and (m6_pos.getValue() <= a6 + 0.01 and m6_pos.getValue() >= a6 - 0.01):
            break
        
def main():
    run_robot()

if __name__ == '__main__':
    main()
