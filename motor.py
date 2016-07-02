
#!/usr/bin/env python
import signal
import socket
import time
import string
import sys
import RPIO.PWM as PWM
import math
import threading
RPIO.setmode(RPIO.BCM)

def initialize()
	in1_pinA =
	in1_pinB = 
	in2_pinA =
	in2_pinB = 
	in3_pinA =
	in3_pinB =
	in4_pinA =
	in4_pinB =


	RPIO.setup(in1_pinA, RPIO.OUT)
	RPIO.setup(in1_pinB, RPIO.OUT)

	RPIO.setup(in2_pinA, RPIO.OUT)
	RPIO.setup(in2_pinB, RPIO.OUT)

	RPIO.setup(in3_pinA, RPIO.OUT)
	RPIO.setup(in3_pinB, RPIO.OUT)

	RPIO.setup(in4_pinA, RPIO.OUT)
	RPIO.setup(in4_pinB, RPIO.OUT)

	RPIO.output(in1_pinA, False)
	RPIO.output(in1_pinB, False)
	RPIO.output(in2_pinA, False)
	RPIO.output(in2_pinB, False)
	RPIO.output(in3_pinA, False)
	RPIO.output(in3_pinB, False)
	RPIO.output(in4_pinA, False)
	RPIO.output(in4_pinB, False)

	PWM.setup(1)
	PWM.init_channel(1, 3000)

def clockwise(pinA, pinB,pwmotor):
	PWM.add_channel_pulse(1,pinA,0,pwmotor)
	PWM.add_channel_pulse(1,pinB,0,0)
def counter_clockwise(pinA, pinB, pwmotor):
	PWM.add_channel_pulse(1,pinA,0,0)
	PWM.add_channel_pulse(1,pinB,0,pwmotor)

def update_velocity(direction1,direction2, direction3,direction4,pwmotor1, pwmotor2, pwmotor3, pwmotor4)
	
	if direction1 == "f":
		clockwise(in1_pinA,in1_pinB,pwmotor1)
	else:
		counter_clockwise(in1_pinA,in1_pinB,pwmotor1)
	if direction2== "f":
		clockwise(in2_pinA,in2_pinB,pwmotor2)
	else: 
		counter_clockwise(in2_pinA,in2_pinB,pwmotor2)
	if direction3== "f":
		clockwise(in3_pinA,in3_pinB,pwmotor3)
	else:
		counter_clockwise(in3_pinA,in3_pinB,pwmotor3)
	if direction4== "f"
		clockwise(in4_pinA,in4_pinB,pwmotor4)
	else:
		counter_clockwise(in4_pinA,in4_pinB,pwmotor4)
	 
