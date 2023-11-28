Dot moves right-left

# Imports go at the top
from microbit import *
import time as t

dot_column = 5
dot_row = 2

while True:
    display.clear()
    if dot_column == 0:
        dot_column = 4
        #display.clear()
    else:
        dot_column -= 1
    display.set_pixel(dot_column,dot_row,9)
    
    t.sleep(0.1)



#dot moves right to left
# Imports go at the top
from microbit import *

#Dot moves right-left

# Imports go at the top
from microbit import *
import time as t

dot_column = 0
dot_row = 4

while True:
    display.clear()
    if dot_column == 4:
        dot_column = 0
        #display.clear()
    else:
        dot_column += 1
    display.set_pixel(dot_column,dot_row,9)
    
    t.sleep(0.1)


Jump animation

# Imports go at the top
from microbit import *
import time as t

dot_column = 2
dot_row = 4
num = 0
still_jump = None


def jump_animation(column, row, speed, row_changer):

    still_jump = True
    
    display.set_pixel(column,row,9)
    row-=row_changer
    t.sleep_ms(100)
    
    display.set_pixel(column,row+1,0)
    
    display.set_pixel(column,row,9)
    t.sleep_ms(100)
    ####

    return [column,row,row_changer]
            
    

    
    array_1 = [0,1,2,3,4]
    array_1[1]


while True:
    if button_a.was_pressed():
        position_info = jump_animation(2,4,1,1)
        while still_jump:
            if position_info[1] >=1:
                #make it jump
            else:
                position_info[2] = -1
                #same make it jump
    



