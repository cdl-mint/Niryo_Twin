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
    scenarios = [
        # Scenario 1
        [
            [0, 0, 0, 0, 0, 0],
            [0.096, -0.592, 0.673, -1.738, -1.499, 0.003],
            [-1.253, -0.592, -0.079, -0.054, -0.750, 0.003],
            [2.495, 0.610, 0.074, 1.770, -1.441, 0.003],
            [0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
            [0, 0, 0, 0, 0, 0]
        ],

        # Scenario 2
        [
            [0, 0, 0, 0, 0, 0],
            [0.00, 0.50, -1.25, 0.00, 0.00, 0.00],
            [0.995, -0.244, 1.0, 0.000, 0.000, -0.007],
            [0.096, -0.592, 0.673, -1.738, -1.499, 0.003],
            [0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
            [0, 0, 0, 0, 0, 0]
        ],

        # Scenario 3
        [
            [0.00, 0.50, -1.25, 0.00, 0.00, 0.00],
            [0, 0, 0, 0, 0, 0],
            [1.253, 0.592, -0.079, -0.054, -0.750, 0.003],
            [0.096, -0.592, 0.673, -1.4, -1.499, 0.003],
            [0.90, 0.5, 0.5, -1.56, 0.0, 0.0],
            [0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
            [0.00, 0.50, -1.25, 0.00, 0.00, 0.00]
        ],

        # Scenario 4
        [
            [0.995, -0.244, 1.0, 0.000, 0.000, -0.007],
            [2.495, 0.610, 0.074, 1.770, -1.441, 0.003],
            [0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
            [-1.253,-0.5,-0.079,-0.054,-0.750,0.003],
            [0.00, 0.20, 0.00, -0.02, -1.4, -0.01],
            [0.096,-0.3,0.673, -1.738, -1.3, 0.003]

        ]
    ]
    for i, scenario in enumerate(scenarios):
        for j in range(2):  # Repeat each scenario 5 times
            print(f"Scenario: {i+1}, range{j+1}")
            file_path = f"logs_scenario_{i+1}_run_{j+1}.txt"  # Define the file path for each scenario run
            with open(file_path, "w") as file:  # Open the file in append mode
                for position in scenario:
                    move_to_position(position, file)

def move_to_position(lis, file):
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
        t2 = datetime.datetime.now()

        # Write position logs to the file
        file.write(str([round(num, 3) for num in position]) + " " + str((t2 - t1).microseconds / 1000) + "\n")

        t1 = t2
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
