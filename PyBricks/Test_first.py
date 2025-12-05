from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch








hub = TechnicHub()

first = Motor(Port.A)
first.run(1500)
print("started")
wait(2000.5)
first.stop()
print("ended")

