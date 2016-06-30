import RPIO
import time

class encoder:
	ENCODER_TICKS_TURN = 20 #number of ticks per full rotation of the shaft
	DEL_TIME = 1 #in seconds
	#pins of the encoder
	A = 0 
	B = 0 
	C = 0
	state=0
	distance=0
	speed=0
	def __init__(self,pinA, pinB, pinC):
		A = pinA
		B = pinB
		C = pinC
		RPIO.setup(7, RPIO.IN, pull_up_down=RPIO.PUD_UP)
		S1 = GPIO.input(A)
		S2 = GPIO.input(B)
		state = S1 + 2*S2
		start_time = time.clock()

	def fsm(old,new):
		table = [0,-1,1,0,
	            1,0,0,-1,
	            -1,0,0,1,
	            0,1,-1,0]
		return table[4*old+new]       
	
	def update():
		newS1 = RPIO.input(A)
		newS2 = RPIO.input(B)
		new_state = newS1 + 2*newS2 		
		rotation = self.fsm(state,new_state) #checks if the state is different from before
		
		distance+=rotation

		if time.clock()-DEL_TIME>start_time:
			speed = steps_for_speed/DEL_TIME
			steps_for_speed = 0
			start_time = time.clock()
		else: 
			steps_for_speed += rotation

		speed =0 #how to estimate the velocity?

	def get_speed():
		return speed
	def get_dist():
		return distance



