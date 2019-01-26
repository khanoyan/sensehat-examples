#!/usr/bin/python3

import time
import numpy as np

from sense_hat import SenseHat
s = SenseHat()

MAX_PIXELS = 25

s.clear()
buf = np.array(s.get_pixels())

while True:
    indexes = np.random.randint(0, 64, MAX_PIXELS)
    for i in indexes:
        buf[i, :] = 255
    s.clear()
    s.set_pixels(buf)
    time.sleep(0.25)
    for i in indexes:
        buf[i, :] = 0
