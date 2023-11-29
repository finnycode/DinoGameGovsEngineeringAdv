# Imports go at the top
from microbit import *
import time as t
import random

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

enemy_column = 4
enemy_rows = [3,4]
enemy_start_time = running_time()
enemy_speed = 500
enemy_choice = 1

display.set_pixel(enemy_column, enemy_rows[0], 9)
display.set_pixel(enemy_column, enemy_rows[1], 9)

            
    
#jump vars
is_jumping = False
jump_height = 0
max_jump_height = 3 

jump_start_time = 0
jump_speed = 200

#move vars
movement_speed = 200  
last_move_time = running_time()

#game vars

score = 0
high_score = 0

collision_detected = False


while not collision_detected:

    current_time = running_time()

    # Jump logic
    pin0_current_state = pin0.is_touched()

    if not pin0_previous_state and pin0_current_state and not is_jumping:
        is_jumping = True
        jump_height = 0
        jump_start_time = current_time

    if is_jumping and current_time > jump_start_time + jump_speed:
        display.set_pixel(dot_column, dot_row, 0)
        if jump_height < max_jump_height:
            dot_row -= 1
            jump_height += 1
        elif dot_row < 4:
            dot_row += 1
            if dot_row == 4:
                is_jumping = False
        display.set_pixel(dot_column, dot_row, 9)
        
        jump_start_time = current_time

    pin0_previous_state = pin0_current_state

   

    
    #right logic
    
    pin2_current_state = pin2.is_touched()
    
    if current_time > last_move_time + movement_speed:
        if not pin2_previous_state and pin2_current_state:
            
            display.set_pixel(dot_column, dot_row, 0)
            if dot_column < 4:
                dot_column += 1
            display.set_pixel(dot_column, dot_row, 9)
            last_move_time = current_time
            
        elif pin2_previous_state and not pin2_current_state:
            pin2_previous_state = False

    pin2_previous_state = pin2_current_state

    

    #left logic
    pin1_current_state = pin1.is_touched()
    
    if current_time > last_move_time + movement_speed:
        if not pin1_previous_state and pin1_current_state:
            display.set_pixel(dot_column, dot_row, 0)
            if dot_column > 0:
                dot_column -= 1
            display.set_pixel(dot_column, dot_row, 9) 
            last_move_time = current_time
            
        elif pin1_previous_state and not pin1_current_state:
            pin1_previous_state = False

    pin1_previous_state = pin1_current_state


    #enemy logic
    
    #add some sort of custom timing thing

    #add random height

    

    if running_time() > enemy_start_time + enemy_speed:
        
    
        display.set_pixel(enemy_column, enemy_rows[0], 0)
        display.set_pixel(enemy_column, enemy_rows[1], 0)
        
        enemy_column -= 1
        
        if enemy_column >= 0:
            
            if enemy_choice == 1:
                
                display.set_pixel(enemy_column, enemy_rows[0], 9)
                display.set_pixel(enemy_column, enemy_rows[1], 9)
                
            elif enemy_choice == 2:

                display.set_pixel(enemy_column, enemy_rows[0], 9)

            elif enemy_choice == 3:
                
                display.set_pixel(enemy_column, enemy_rows[1], 9)
    
        else:
            score+=1
            enemy_column = 4
            
            enemy_choice = random.randint(1,3)

            if enemy_choice == 1:
                
                display.set_pixel(enemy_column, enemy_rows[0], 9)
                display.set_pixel(enemy_column, enemy_rows[1], 9)
                
            elif enemy_choice == 2:

                display.set_pixel(enemy_column, enemy_rows[0], 9)

            elif enemy_choice == 3:
                
                display.set_pixel(enemy_column, enemy_rows[1], 9)
                
                
        enemy_start_time = current_time

        #collision detection

        if enemy_choice == 1:

            if dot_column == enemy_column:
                if dot_row == enemy_rows[0] or dot_row == enemy_rows[1]: 
                    
                    collision_detected = True
                
        elif enemy_choice == 2:

            if dot_column == enemy_column:
                if dot_row == enemy_rows[0]: 
                    
                    collision_detected = True

        elif enemy_choice == 3:
                
            if dot_column == enemy_column:
                if dot_row == enemy_rows[1]: 
                    
                    collision_detected = True    

if collision_detected:
    display.clear()
    display.show(Image.SAD)

    
    



