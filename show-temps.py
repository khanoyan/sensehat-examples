#!/usr/bin/python3

from sense_hat import SenseHat
import time
import numpy as np

s = SenseHat()

s.clear()

from bs4 import BeautifulSoup
import requests

def c2f(degC):
    return degC * 1.8 + 32

def displayLED(insideTemp, outsideTemp):
    s.show_message(text_string="{:d}F".format(int(outsideTemp)), 
        scroll_speed=0.05,
        text_colour=[255,255,255],
        back_colour=[0,0,0])
    s.show_message(text_string="{:d}F".format(int(insideTemp)), 
        scroll_speed=0.05,
        back_colour=[127,127,127],
        text_colour=[0,0,0])

resp = requests.get('http://w1.weather.gov/xml/current_obs/KBUR.xml')

soup = BeautifulSoup(resp.text, 'lxml')

allTags = soup.findAll(True)
allTagNames = [tag.name for tag in allTags]
allTagValues = [tag.string for tag in allTags]

# fetch outside temp only once (for now)
outsideTemp = float(soup.temp_f.string)

while True:
    insideTemp = c2f(s.temp)
    print("Outside temperature is {:.1f} degrees F.".format(outsideTemp))
    print("Inside temperature is {:.1f} degrees F.".format(insideTemp))
    displayLED(insideTemp=insideTemp, outsideTemp=outsideTemp)


