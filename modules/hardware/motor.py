
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
	import RPIO.PWM as PWM
	result = None
	for i in range(0,15):
		if not PWM.is_channel_initialized(i):
			result = i
			break
	if result == None:
		raise ValueError('No DMA channel available, error')
	return result

def get_DMA():
	a = find_DMA_available()
	PWM.init_channel(a)
	return a

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
			dma_ch1 = get_DMA()
			dma_ch2 = get_DMA()
			self.motor_list.append([[pin1,pin2],[dma_ch1,dma_ch2]])
		
		def set_velocity(self,pwmotor,motor_id):
			[pins,dma_ch] = self.motor_list[motor_id]
			c = [0,0]
			c[0] = PWM.get_channel_subcycle_time_us(dma_ch[0])/(100.0*PWM.get_pulse_incr_us()) #coefficient to convert duty to period
			c[1] = PWM.get_channel_subcycle_time_us(dma_ch[1])/(100.0*PWM.get_pulse_incr_us()) #coefficient to convert duty to period
			try:
				PWM.clear_channel_gpio(dma_ch[0], pins[0])
				PWM.clear_channel_gpio(dma_ch[1], pins[1])
			except:
				pass
			if pwmotor>0:
				PWM.add_channel_pulse(dma_ch[1],pins[1],0,0)
				PWM.add_channel_pulse(dma_ch[0],pins[0],0,int(abs(pwmotor)*c[0]))
			else:
				PWM.add_channel_pulse(dma_ch[0],pins[0],0,0)
				PWM.add_channel_pulse(dma_ch[1],pins[1],0,int(abs(pwmotor)*c[1]))



