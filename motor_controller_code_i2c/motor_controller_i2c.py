from smbus import SMBus
import time


bus = SMBus(1) 
arduinoAddress = 12


step_total = 20
step_count = 0

throttle_max = 255
throttle_min = 0
throttle_step = int((throttle_max - throttle_min) / step_total)

steering_max = 130
steering_min = 50
steering_step = int((steering_max - steering_min) / step_total)

throttle_val = throttle_min
steering_val = steering_min


while True:
	
	while step_count < step_total:
		bus.write_i2c_block_data(arduinoAddress, 1, [throttle_val, steering_val])
		throttle_val += throttle_step
		steering_val += steering_step
		step_count += 1
		print("throttle: " + str(throttle_val) + ", steering: " + str(steering_val))
		time.sleep(0.5)

	while step_count > 0:
		bus.write_i2c_block_data(arduinoAddress, 1, [throttle_val, steering_val])
		time.sleep(0.1)
		throttle_val -= throttle_step
		steering_val -= steering_step
		step_count -= 1
		print("throttle: " + str(throttle_val) + ", steering: " + str(steering_val))
		time.sleep(0.5)