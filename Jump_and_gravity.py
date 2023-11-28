# Jumping
from microbit import *
import time as t 
import random
x = 2
y = 4
character = display.set_pixel(x,y,9)
pin0_previous_state = False
jumping = False 
y_gravity = .2
Jump_height = 2
y_velocity = Jump_height

pin0.set_touch_mode(pin0.RESISTIVE)
while True:
    pin0_current_state = pin0.is_touched()
    if not pin0_previous_state:
         jumping = True
    if jumping:
            y -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < -Jump_height:
                jumping = False
                y_velocity = Jump_height

    elif pin0_previous_state and not pin0_current_state:
        pin0_previous_state = False
