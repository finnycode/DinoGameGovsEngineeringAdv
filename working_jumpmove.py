# Imports go at the top
from microbit import *
import time as t

# Initial state of the pins
pin2_previous_state = False
pin1_previous_state = False
pin0_previous_state = False

pin1.set_touch_mode(pin1.RESISTIVE)
pin2.set_touch_mode(pin2.RESISTIVE)
pin0.set_touch_mode(pin0.RESISTIVE)

dot_column = 2
dot_row = 4
display.set_pixel(dot_column, dot_row, 9)



            
    
# Jump variables
is_jumping = False
jump_height = 0
max_jump_height = 3  # Adjust as needed

while True:
    # Jump logic
    pin0_current_state = pin0.is_touched()

    if not pin0_previous_state and pin0_current_state and not is_jumping:
        is_jumping = True
        jump_height = 0

    if is_jumping:
        display.set_pixel(dot_column, dot_row, 0)
        if jump_height < max_jump_height:
            dot_row -= 1
            jump_height += 1
        elif dot_row < 4:
            dot_row += 1
            if dot_row == 4:
                is_jumping = False
        display.set_pixel(dot_column, dot_row, 9)

    pin0_previous_state = pin0_current_state

   

    
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

    t.sleep(0.1)



