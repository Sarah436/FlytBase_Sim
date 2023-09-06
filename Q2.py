#!/usr/bin/env python
#Imports and initialization
import time
from flyt_python import api

#  instance of flyt droneigation class
drone = api.navigation(timeout=120000)

time.sleep(3)

# Take off to an altitude of 10 meters
print('Taking off to 10m')
drone.take_off(10.0)

# triangle trajectory wit a side length of 10 meters at a height of 10 meters
print('Moving along the triangle trajectory')
drone.position_set(10, 0, 0, relative=True)
time.sleep(1)
drone.position_set(-5, 8.7, 0, relative=True)
time.sleep(1)
drone.position_set(-5, -8.7, 0, relative=True)
time.sleep(1)

#Interface shutdown
print('Landing')
drone.land(async=False)

#shutdown the instance
drone.disconnect()

