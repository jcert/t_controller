
#!/usr/bin/env python
import signal
import socket
import time
import string
import sys
import RPIO
import RPIO.PWM as PWM
import math
import threading



class motor: #has all motors in one class, what about the 2 wheels and caster? would've been better to make a class for motors, one for driver (w/ 2 motors in) and then a super-class w/ 2 driver in it.
	def __init__(self):
		print "will this show?motor.motor.init"
		try :
			PWM.setup(1) #put this in def __init__():
		except :
			pass
		PWM.init_channel(3, 3000)
	class driver:
		def __init__(self):
			self.motor_list=[]
			
		def add_motor(self,pin1,pin2):
	        	#self.pinA=pin1
	        	#self.pinB=pin2
			self.motor_list.append([pin1,pin2])
			
			
		
		def set_velocity(self,pwmotor,motor_id):
			pins = self.motor_list[motor_id]
			if pwmotor>0:
				PWM.add_channel_pulse(3,pins[0],0,pwmotor)
				PWM.add_channel_pulse(3,pins[1],0,0)
				
			else:
				PWM.add_channel_pulse(2,pins[0],0,0)
				PWM.add_channel_pulse(2,pins[1],0,pwmotor)



