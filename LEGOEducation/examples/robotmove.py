# Double Motor Example
import legoeducation as le
import time
import math

# update these values to match the Connection Card
card_color = le.LEGO_COLOR_YELLOW
card_serial = '0293'
wheel_diameter = 63 #in_mm

def distance_calculator(distance_in_mm):
	degrees_to_move = 360/(math.pi * wheel_diameter) * distance_in_mm
	return degrees_to_move

def move_forward(distance_in_mm, motor_speed):
	degrees_to_move = distance_calculator(distance_in_mm)
	print(f"Moving forward {distance_in_mm} mm, which is {degrees_to_move} degrees.")
	doublemotor.movement_move_for_degrees(degrees_to_move, direction=le.MOVEMENT_MOVE_DIRECTION_FORWARD, speed=motor_speed)

def move_backward(distance_in_mm, motor_speed):
	degrees_to_move = distance_calculator(distance_in_mm)
	print(f"Moving backward {distance_in_mm} mm, which is {degrees_to_move} degrees.")
	doublemotor.movement_move_for_degrees(degrees_to_move, direction=le.MOVEMENT_MOVE_DIRECTION_BACKWARD, speed=motor_speed)

def turn_right(degrees_to_move, motor_speed):
	doublemotor.movement_turn_for_degrees(degrees_to_move, speed=motor_speed)

def turn_left(degrees_to_move, motor_speed):
	doublemotor.movement_turn_for_degrees(-degrees_to_move, speed=motor_speed)


# Connect to the Double Motor
doublemotor = le.DoubleMotor()
doublemotor.connect(card_color=card_color, card_serial=card_serial)

# Check connection
if not doublemotor.connected:
	print('Error connecting to Double Motor.')
	exit(1) # error connecting

# Example:
# - go forward
# - turn 90-degrees
# - repeat that 4 times (a square)
""" for i in range(4):
	doublemotor.movement_move_for_time(1000, speed=30)
	doublemotor.movement_turn_for_degrees(90)
 """
move_forward(200, motor_speed=100)
turn_right(90, motor_speed=30)
turn_left(90, motor_speed=30)	
move_backward(200, motor_speed=20)

doublemotor.movement_stop()
# Disconnect
doublemotor.disconnect()
exit(0) # successful execution