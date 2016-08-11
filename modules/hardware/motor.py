
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

def find_DMA_available():
	result = None
	for i in range(0,15):
		if is_channel_initialized(i):
			result = i
			break
	if result == None:
		raise ValueError('No DMA channel available, error')
	return result

class motor: #has all motors in one class, what about the 2 wheels and caster? would've been better to make a class for motors, one for driver (w/ 2 motors in) and then a super-class w/ 2 driver in it.
	def __init__(self):
		if not PWM.is_setup():
			PWM.setup() #put this in def __init__():
		#the channel is individual to each pwm signal
	class driver:
		def __init__(self):
			self.motor_list=[]
			
		def add_motor(self,pin1,pin2):
	        	#self.pinA=pin1
	        	#self.pinB=pin2
			dma_channel = find_DMA_available()
			PWM.init_channel(dma_channel)
			self.motor_list.append([[pin1,pin2],dma_channel])
		
		def set_velocity(self,pwmotor,motor_id):
			[pins,dma_channel] = self.motor_list[motor_id]
			c = get_channel_subcycle_time_us(0)/100.0 #coefficient to convert duty to period
			PWM.clear_channel_gpio(0, pins[0])
			PWM.clear_channel_gpio(0, pins[1])
			if pwmotor>0:
				PWM.add_channel_pulse(0,pins[1],0,0)
				PWM.add_channel_pulse(0,pins[0],0,abs(pwmotor)*c)
			else:
				PWM.add_channel_pulse(0,pins[0],0,0)
				PWM.add_channel_pulse(0,pins[1],0,abs(pwmotor)*c)



