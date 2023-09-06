#!/usr/bin/env python
#Imports and initialization
import time
from flyt_python import api

# instance of flyt droneigation class
drone = api.navigation(timeout=120000)


time.sleep(3)

# Take off to an altitude of 10 meters
print('Taking off')
drone.take_off(5.0)

#  square trajectory with a side length of 6.5 meters
print('Moving along the setpoints')
drone.position_set(6.5, 0, 0, relative=True)
drone.position_set(0, 6.5, 0, relative=True)
drone.position_set(-6.5, 0, 0, relative=True)
drone.position_set(0, -6.5, 0, relative=True)

# Interface shutdown
print('Landing')
drone.land(async=False)

#shutdown the instance
drone.disconnect()

