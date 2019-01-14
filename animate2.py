#!/usr/bin/python3

from sense_hat import SenseHat
import time
import numpy as np
import random
s = SenseHat()

once = True

def fun(i):
    r = random.randrange(-25, 25)
    if (i+r < 0):
        return 0
    elif (i+r > 255):
        return 255
    else:
        return i+r
    # return (abs(i+r)%255)

j = 0
while True:
    x = np.linspace(0+(j/100), np.pi+(j/100), 64)
    y = np.int32(np.floor(np.abs(np.sin(x)*255)))
    #patt = [(i,i,i) for i in y]
    patt = [(fun(i), fun(i), fun(i)) for i in y]
    s.set_pixels(patt)
    time.sleep(.005)
    j += 1
    if once:
        once = False
        print(patt)
        print(len(y))
        print(len(patt))

