from hardware import motor
import time


	#pin config the motor driver
#create object for motors

#create object driver, that can serve up to two motors

#add to driver object one motor, giving the pin used for the connection

#spin the motor with increasing speed, make transitions every X seconds

#spin in reverse direction, same time between speed changes

RPIO.PWM.setup(1)
PWM.init_channel(3,3000)
#PWM.add_channel_pulse(3,16,0,2000)
mot1     = motor.motor()
driver1  = mot1.driver()
driver1.add_motor(16,19)

cycling=True
while cycling:
   res=raw_input()
   if res=='1':
      driver1.set_velocity(200,0)
      print "mememememe"
      PWM.print_channel(3)

   if res=='0':
      PWM.clear_channel(3)
      cycling=False








