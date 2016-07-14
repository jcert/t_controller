from hardware import motor
import time



	#pin config the motor driver
#create object driver, that can serve up to two motors
driver = motor.driver()

#add to driver object one motor, giving the pin used for the connection
motor1 = driver.add_motor(m1a,m1b)

#spin the motor with increasing speed, make transitions every X seconds
for i in range(0,MAX_MOTOR):
	motor1.set_velocity(i)
	time.sleep(TRANSITION_TIME)

#spin in reverse direction, same time between speed changes
for i in range(0,MAX_MOTOR):
	motor1.set_velocity(-i)
	time.sleep(TRANSITION_TIME)






