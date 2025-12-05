from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import Car
from pybricks.tools import wait

# Set up all devices.
steering = Motor(Port.B, Direction.CLOCKWISE)
front = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rear = Motor(Port.A, Direction.COUNTERCLOCKWISE)
car = Car(steering, [front, rear])
xbox = XboxController()

#test
# front.run(200)
# wait(1500)
# front.stop()

# The main program starts here.
while True:
    # Control steering using the right joystick.
    car.steer(xbox.joystick_right()[0])
    # Control drive power using left joystick.
    car.drive_power(xbox.joystick_left()[1])

    # Control drive power using the trigger buttons.
    # car.drive_power(xbox.triggers()[1] - xbox.triggers()[0])
    wait(50)
