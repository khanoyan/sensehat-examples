#!/usr/bin/python3

from sense_hat import SenseHat
import time

s = SenseHat()

fnames = []
for i in range(5):
    fnames.append("g{}.png".format(i))

## OR

# list comprehension ?
fnames = ['g{}.png'.format(i) for i in range(5)]

## or
fnames = ['g%d.png' %(i) for i in range(5)]

for i in range(10):
    for fname in fnames:
        s.load_image(fname)
        time.sleep(0.1)
        
