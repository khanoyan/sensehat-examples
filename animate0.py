#!/usr/bin/python3

from sense_hat import SenseHat
import time
import numpy as np

s = SenseHat()

#clear display
s.clear()

# set corner pixel to red
s.set_pixel(0, 0, 255, 0, 0)

# rotate pixel around display
for i in range(2):
    s.flip_h();
    time.sleep(.25)
    s.flip_v();
    time.sleep(0.25)


# clear again
s.clear()

# get empty display buffer
buf = s.get_pixels()

# make a 'clear' numpy array from buf
# to use later
cl = np.array(buf)

# change pixel 1 to blue and refresh
buf[1][2] = 255
s.set_pixels(buf)
time.sleep(1)

# clear with the saved np array
s.set_pixels(cl)
time.sleep(1)

# let's get a fresh np buffer array
buf = np.copy(cl)

# turn all pixels green
buf[: , 1] = 255
s.set_pixels(buf)
time.sleep(1)

# change np array to 2D
buf = buf.reshape((8, 8, 3))
# set last pixel to white
buf[7, 7, :] = 255
buf = buf.reshape((64, 3))
s.set_pixels(buf)
time.sleep(1)

# set all pixels to blue
buf = np.copy(cl)
buf[: , 2] = 255
s.set_pixels(buf)
time.sleep(1)

# *advanced* set middle to white
buf = buf.reshape((8, 8, 3))
buf[2:6, 2:6, :] = 255
buf = buf.reshape((64, 3))
s.set_pixels(buf)

