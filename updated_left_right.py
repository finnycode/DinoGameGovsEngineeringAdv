# Imports go at the top
from microbit import *
import time as t

# Initial state of the pins
pin2_previous_state = False
pin1_previous_state = False

pin1.set_touch_mode(pin1.RESISTIVE)
pin2.set_touch_mode(pin2.RESISTIVE)

dot_column = 2
dot_row = 4
display.set_pixel(dot_column, dot_row, 9)

while True:
    
    #right logic
    
    pin2_current_state = pin2.is_touched()

    if not pin2_previous_state and pin2_current_state:
        
        display.set_pixel(dot_column, dot_row, 0)
        if dot_column < 4:
            dot_column += 1
        display.set_pixel(dot_column, dot_row, 9)
    elif pin2_previous_state and not pin2_current_state:
        pin2_previous_state = False

    pin2_previous_state = pin2_current_state

    pin1_current_state = pin1.is_touched()

    #left logic
    
    if not pin1_previous_state and pin1_current_state:
        display.set_pixel(dot_column, dot_row, 0)
        if dot_column > 0:
            dot_column -= 1
        display.set_pixel(dot_column, dot_row, 9) 
    elif pin1_previous_state and not pin1_current_state:
        pin1_previous_state = False

    pin1_previous_state = pin1_current_state

    t.sleep(0.2)



