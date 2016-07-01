import RPIO #gpio library of choice, gives us better pwm
import time

class encoders:
	FREQ = 100 # sampling frequency for the encoders 
	connected_encoders = [] 
	def __init__(self,pinA, pinB): #pin A and B will be global
		A = pinA #read pin #maybe the reading pins could be global and the C be an address, would save many pins
		B = pinB #read pin
		RPIO.setup(A, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
		RPIO.setup(B, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
	def update_loop(self):
		while True:
			self.update
			time.sleep(1.0/FREQ)

	def update():
		for i in connected_encoders:
			i.update()

	class encoder:
		ENCODER_TICKS_TURN = 20 #number of ticks per full rotation of the shaft
		DEL_TIME = 1 #in seconds
		#pins of the encoder
		def __init__(self,pinC):
			self.C = pinC #write pin
			self.S1 = GPIO.input(A)
			self.S2 = GPIO.input(B)
			self.state = S1 + 2*S2
			self.start_time = time.clock()
			connected_encoders.append(self)
		def fsm(old,new):
			table = [0,-1,1,0,
						1,0,0,-1,
						-1,0,0,1,
						0,1,-1,0]
			return table[4*old+new]       
		
		def update():

			#correponding C pin to output
			#corresponding C pin to HIGH
			RPIO.setup(self.C, RPIO.OUT)
			RPIO.output(self.c, True)
			self.newS1 = RPIO.input(A)
			self.newS2 = RPIO.input(B)
			RPIO.setup(self.C, RPIO.IN)
			#after reading, go back to high impedance, should check if this is pull-down or at least floating
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



