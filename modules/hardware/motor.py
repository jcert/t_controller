
#!/usr/bin/env python
#import signal
#import socket
#import time
#import string
#import sys
import RPIO
import RPIO.PWM as PWM
import math
import threading



class motor: #has all motors in one class, what about the 2 wheels and caster? would've been better to make a class for motors, one for driver (w/ 2 motors in) and then a super-class w/ 2 driver in it.
	def __init__(self):
		if not PWM.is_setup():
			PWM.setup() #put this in def __init__():
    	if not is_channel_initialized(0):
			PWM.init_channel(0)
	class driver:
		def __init__(self):
			self.motor_list=[]
			
		def add_motor(self,pin1,pin2):
	        	#self.pinA=pin1
	        	#self.pinB=pin2
			self.motor_list.append([pin1,pin2])
		
		def set_velocity(self,pwmotor,motor_id):
			pins = self.motor_list[motor_id]
			c = get_channel_subcycle_time_us(0)/100.0 #coefficient to convert duty to period
			if pwmotor>0:
				PWM.add_channel_pulse(0,pins[0],0,abs(pwmotor)*c)
				PWM.add_channel_pulse(0,pins[1],0,0)
				
			else:
				PWM.add_channel_pulse(0,pins[0],0,0)
				PWM.add_channel_pulse(0,pins[1],0,abs(pwmotor)*c)



