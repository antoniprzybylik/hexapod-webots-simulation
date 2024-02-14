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

class Leg:
    def __init__(self, s1, s2, s3, offset, leg_name: str, sign):
        self._s1 = s1
        self._s2 = s2
        self._s3 = s3
        self._offset = offset
        self._leg_name = leg_name
        self._sign = sign

    def __str__(self):
        return self._leg_name

    def move_leg(self):
        print(1)
        self._s2.setPosition(math.pi/5)
        yield 2
        print(2)
        print(self._offset + (math.pi / 6)*self._sign)
        self._s1.setPosition(self._offset + (math.pi / 6)*self._sign)
        yield 2
        print(3)
        self._s2.setPosition(math.pi / 6 - 0.01)
        yield 2
        print(4)
        self._s1.setPosition(self._offset)
        yield 3
        self._s2.setPosition(math.pi / 6)


def test():
    #L2 Swing
    print("Fist phase")
    #servo22.setPosition(math.pi/7)
    yield 1
    print("Second phase")
    servo21.setPosition(math.pi/6)
    yield 2
    print("Third phase")
    servo21.setPosition(-math.pi/6)
    yield 3





t1 = time()
leg1 = Leg(servo11, servo12, servo13, 0, "l1", -1)
leg2 = Leg(servo21, servo22, servo23, 0, "l2", -1)
leg3 = Leg(servo31, servo32, servo33, 0, "l3", -1)
leg4 = Leg(servo41, servo42, servo43, math.pi, "l4", 1)
leg5 = Leg(servo51, servo52, servo53, math.pi, "l5", 1)
leg6 = Leg(servo61, servo62, servo63, math.pi, "l6", 1)

leg_list = [leg1, leg4, leg2, leg5, leg3, leg6]

leg = leg_list.pop()
print(leg)
g = leg.move_leg()

while robot.step(timestep) != -1:
    if time() - t1 >= 0.1:
        try:
            next(g)
        except:
            leg_list.insert(0, leg)
            leg = leg_list.pop()
            print(leg)
            g = leg.move_leg()
        t1 = time()
    pass

# Enter here exit cleanup code.
