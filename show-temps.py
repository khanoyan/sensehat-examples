#!/usr/bin/python3

from sense_hat import SenseHat
import time
import numpy as np

s = SenseHat()

s.clear()

from bs4 import BeautifulSoup
import requests

resp = requests.get('http://w1.weather.gov/xml/current_obs/KBUR.xml')

soup = BeautifulSoup(resp.text, 'lxml')

allTags = soup.findAll(True)
allTagNames = [tag.name for tag in allTags]
allTagValues = [tag.string for tag in allTags]


outsidetemp = float(soup.temp_f.string)

insidetemp = s.temp * 1.8 + 32

print("Outside temperature is {:.1f} degrees F.".format(outsidetemp))
print("Inside temperature is {:.1f} degrees F.".format(insidetemp))
