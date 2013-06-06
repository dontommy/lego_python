#!/usr/bin/python
'''
Created on May 3, 2013

@author: dontommy
'''
import nxt.locator
from nxt.motor import *
from nxt.sensor import *

def spin_around(b):
    m_left = Motor(b, PORT_B)
    m_left.turn(100, 360)
    m_right = Motor(b, PORT_C)
    m_right.turn(100, 360)


#brick = sock.connect()
#lys = Light(b, PORT_3).get_sample()
b = nxt.locator.find_one_brick()

#spin_around(b)


tryk = Touch(b, PORT_1).get_sample())
while tryk == True:
    spin_around(b)


