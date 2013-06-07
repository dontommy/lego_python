#!/usr/bin/env python

import nxt.locator
from nxt.motor import *
from nxt.sensor import *

b = nxt.locator.find_one_brick()

#print 'Touch:', Touch(b, PORT_1).get_sample()
def spin_around(b):
    m_left = Motor(b, PORT_B)
    m_left.turn(-100, 360)
    m_right = Motor(b, PORT_C)
    m_right.turn(-100, 360)

while True:
    thet = Light(b, PORT_1).get_sample()
    print(thet)
    if thet == True:
        spin_around(b)
    else:
        continue