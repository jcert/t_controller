import RPIO
import time

class encoder:
	ENCODER_TICKS_TURN = 20 #number of ticks per full rotation of the shaft
	DEL_TIME = 1 #in seconds
	#pins of the encoder
	def __init__(self,pinA, pinB, pinC):
		self.A = pinA
		self.B = pinB
		self.C = pinC

		RPIO.setup(7, RPIO.IN, pull_up_down=RPIO.PUD_UP)
		

		self.S1 = GPIO.input(A)
		self.S2 = GPIO.input(B)
		self.state = S1 + 2*S2
		self.start_time = time.clock()

	def fsm(old,new):
		table = [0,-1,1,0,
	            1,0,0,-1,
	            -1,0,0,1,
	            0,1,-1,0]
		return table[4*old+new]       
	
	def update():
		self.newS1 = RPIO.input(A)
		self.newS2 = RPIO.input(B)
		self.new_state = newS1 + 2*newS2 		
		self.rotation = self.fsm(state,new_state) #checks if the state is different from before
		
		self.distance+=self.rotation

		if time.clock()-DEL_TIME>self.start_time:
			self.speed = self.steps_for_speed/DEL_TIME
			self.steps_for_speed = 0
			self.start_time = time.clock()
		else: 
			self.steps_for_speed += self.rotation

	def get_speed():
		return self.speed
	def get_dist():
		return self.distance



