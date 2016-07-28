
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
import RPi.GPIO as GPIO


class motor: #has all motors in one class, what about the 2 wheels and caster? would've been better to make a class for motors, one for driver (w/ 2 motors in) and then a super-class w/ 2 driver in it.
	def __init__(self):
		
		
		RPIO.setmode(RPIO.BCM)
		PWM.setup(10,0)#put this in def __init__():
		PWM.init_channel(2, 100000)
	class driver:
		def __init__(self):
			self.motor_list=[]
			
		def add_motor(self,pin1,pin2):
	        	#self.pinA=pin1
	        	#self.pinB=pin2
			print "okokokokok",pin1
			self.motor_list.append([pin1,pin2])
			
			
		
		def set_velocity(self,pwmotor,motor_id):
			pins = self.motor_list[motor_id]
			if pwmotor>0:
				print "kkkkkkkk", pins[0]
				PWM.add_channel_pulse(2,pins[0],0,pwmotor)
				PWM.add_channel_pulse(2,pins[1],0,0)
			else:
				PWM.add_channel_pulse(2,pins[0],0,0)
				PWM.add_channel_pulse(2,pins[1],0,pwmotor)
GPIO.setmode(GPIO.BOARD)

mot1=motor()
driver1=mot1.driver()
driver1.add_motor(40,19)

cycling=True
while cycling:
	res=raw_input()
	if res=='1':
		driver1.set_velocity(2000,0)
		print "mememememe"
		PWM.print_channel(2)
		
	if res=='0':
		PWM.clear_channel(2)
		cycling=False


