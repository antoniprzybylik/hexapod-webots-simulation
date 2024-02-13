"""basic_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
from time import sleep, time
import math
# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
servo11 = robot.getDevice("Servo11")
servo12 = robot.getDevice("Servo12")
servo13 = robot.getDevice("Servo13")

servo21 = robot.getDevice("Servo21")
servo22 = robot.getDevice("Servo22")
servo23 = robot.getDevice("Servo23")

servo31 = robot.getDevice("Servo31")
servo32 = robot.getDevice("Servo32")
servo33 = robot.getDevice("Servo33")

servo41 = robot.getDevice("Servo41")
servo42 = robot.getDevice("Servo42")
servo43 = robot.getDevice("Servo43")

servo51 = robot.getDevice("Servo51")
servo52 = robot.getDevice("Servo52")
servo53 = robot.getDevice("Servo53")

servo61 = robot.getDevice("Servo61")
servo62 = robot.getDevice("Servo62")
servo63 = robot.getDevice("Servo63")



servo12.setPosition(math.pi/6)
servo13.setPosition(-math.pi/2)

servo22.setPosition(math.pi/6)
servo23.setPosition(-math.pi/2)

servo32.setPosition(math.pi/6)
servo33.setPosition(-math.pi/2)

servo42.setPosition(math.pi/6)
servo43.setPosition(-math.pi/2)

servo52.setPosition(math.pi/6)
servo53.setPosition(-math.pi/2)

servo62.setPosition(math.pi/6)
servo63.setPosition(-math.pi/2)

def test():
    #L2 Swing
    print("Fist phase")
    servo22.setPosition(math.pi/7)
    yield 1
    print("Second phase")
    servo21.setPosition(math.pi/6)
    yield 2
    print("Third phase")
    servo21.setPosition(-math.pi/6)
    yield 3



# Main loop:
# - perform simulation steps until Webots is stopping the controller
t1 = time()
x = test()
i = 0
while robot.step(timestep) != -1:
    print(time() - t1)
    if time() - t1 >= 5 and i < 3:
        next(x)
        t1 = time()
        i += 1

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
