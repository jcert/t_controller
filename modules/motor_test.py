from hardware import motor
import time


	#pin config the motor driver
#create object for motors

#create object driver, that can serve up to two motors

#add to driver object one motor, giving the pin used for the connection

#spin the motor with increasing speed, make transitions every X seconds

#spin in reverse direction, same time between speed changes


#<this has to be moved into the motor module
#RPIO.PWM.setup(1)
#PWM.init_channel(3,3000)
#/>
#PWM.add_channel_pulse(3,16,0,2000) #this should not even be around? what is it for?
mot1     = motor.motor()
driver1  = mot1.driver()
driver1.add_motor(16,19)

cycling=True
print "a - abort; h - this help menu; <number> - set velocity to it"
while cycling:
   res=raw_input()
   if res=='a':
      cycling=False
   elif res=='h':
      print "a - abort; h - this help menu; <number> - set velocity to it"
   else:
      res = int(res)	      
      driver1.set_velocity(res,0)
#      PWM.print_channel(3)
#     PWM.clear_channel(3)








