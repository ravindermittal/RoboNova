# Single Motor Example
import legoeducation as le
import time
import colorsys

# update these values to match the Connection Card
card_color = le.LEGO_COLOR_YELLOW
card_serial = '0293'

# Connect to the Single Motor
singlemotor = le.SingleMotor()
singlemotor.connect(card_color=card_color, card_serial=card_serial)
# Connect to the Color Sensor
colorsensor = le.ColorSensor()
colorsensor.connect(card_color=card_color, card_serial=card_serial)

# Check connection
if not colorsensor.connected:
	print('Error connecting to Color Sensor.')
	exit(1) # error connecting
else:
	print('Color Sensor connected successfully.')

# Check connection
if not singlemotor.connected:
	print('Error connecting to Single Motor.')
	exit(1) # error connecting
else:
	print('Single Motor connected successfully.')

# Example:
# - for five seconds: stream RGB values
# - look at RGB values and print "Red" if color is red
print('looking for colors:')


# Example:
# - Reset single motor relative position (to 0)
# - Start running single motor slow (speed 20%)
# - Check single motor position for 5 seconds
# - If single motor position is greater than 360, fun fast (speed 80%)

singlemotor.motor_reset_relative_position()

singlemotor.motor_run(speed=20)

for i in range(500):
	print(f'Current position: {singlemotor.motor.position}')
	if (colorsensor.sensor.color == le.LEGO_COLOR_RED):
		print('Color is RED, running motor fast!')
		singlemotor.motor_run(speed=80)
	elif (colorsensor.sensor.color == le.LEGO_COLOR_WHITE):
		singlemotor.motor_run(speed=30)
		print('Color is WHITE, running motor slow!')
	time.sleep(0.1) # 1/10th of a second

singlemotor.motor_stop()
# Disconnect
colorsensor.disconnect()
singlemotor.disconnect()
exit(0) # successful execution