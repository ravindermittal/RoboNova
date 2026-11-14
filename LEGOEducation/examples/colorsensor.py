# Color Sensor Example
import legoeducation as le
import time
import colorsys

# update these values to match the Connection Card
card_color = le.LEGO_COLOR_YELLOW
card_serial = '0293'

# Connect to the Color Sensor
colorsensor = le.ColorSensor()
colorsensor.connect(card_color=card_color, card_serial=card_serial)

# Check connection
if not colorsensor.connected:
	print('Error connecting to Color Sensor.')
	exit(1) # error connecting

# Example:
# - for five seconds: stream RGB values
# - look at RGB values and print "Red" if color is red
print('looking for colors:')

def color_name(red, green, blue):
	brightness = max(red, green, blue)
	if brightness < 20:
		return 'BLACK'

	# Normalize brightness so the hue is still useful in different lighting.
	maximum = float(brightness)
	normalized = tuple(channel / maximum for channel in (red, green, blue))
	hue, saturation, _ = colorsys.rgb_to_hsv(*normalized)
	if saturation < 0.2:
		return 'WHITE'

	hue_degrees = hue * 360
	color_hues = {
		'RED': 0,
		'ORANGE': 30,
		'YELLOW': 60,
		'GREEN': 120,
		'TEAL': 165,
		'AQUA': 185,
		'AZURE': 210,
		'BLUE': 240,
		'PURPLE': 280,
		'PINK': 330,
	}
	return min(
		color_hues,
		key=lambda name: min(
			abs(hue_degrees - color_hues[name]),
			360 - abs(hue_degrees - color_hues[name]),
		),
	)

for i in range(2000):
	# stream 
	R = colorsensor.sensor.rawRed
	G = colorsensor.sensor.rawGreen
	B = colorsensor.sensor.rawBlue
	
	print(f'RGB: {(R, G, B)}')
	print(f'Color: {color_name(R, G, B)}')
	time.sleep(0.1)

# Disconnect
colorsensor.disconnect()
exit(0) # successful execution