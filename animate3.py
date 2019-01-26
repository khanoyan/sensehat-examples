#!/usr/bin/python3

import time
import numpy as np

from sense_hat import SenseHat
s = SenseHat()

s.clear()

i = 0
increase = True

while True:
    s.set_pixel(i, 0, (255, 255, 255))
    time.sleep(0.1)
    s.set_pixel(i, 0, (0, 0, 0))
    if increase:
        i += 1
        if i+1 == 8:
            increase = False
    else:
        i -= 1
        if i-1 == -1:
            increase = True
