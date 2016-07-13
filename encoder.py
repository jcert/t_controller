import RPIO #gpio library of choice, gives us better pwm
import time

class encoders:
	FREQ = 100 # sampling frequency for the encoders 
	connected_encoders = [] 
	a = 0
	b = 0
	def __init__(self,pinA, pinB): #pin A and B will be global
		encoders.a = pinA #read pin #maybe the reading pins could be global and the C be an address, would save many pins
		encoders.b = pinB #read pin
		print encoders.a, encoders.b
		RPIO.setmode(RPIO.BCM)
		RPIO.setup(encoders.a, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
		RPIO.setup(encoders.b, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
	def update_loop(self):
		while True:
			self.update
			time.sleep(1.0/FREQ)

	def update(self):
		for i in encoders.connected_encoders:
			i.update()

class encoder(encoders):

	ENCODER_TICKS_TURN = 20 #number of ticks per full rotation of the shaft
	DEL_TIME = 1 #in seconds
	#pins of the encoder
	def __init__(self,pinC):
		self.c = pinC #write pin
		print encoders.a,encoders.b
		RPIO.setup(encoders.a, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
		RPIO.setup(encoders.b, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
		self.S1 = RPIO.input(encoders.a)
		self.S2 = RPIO.input(encoders.b)
		self.state = self.S1 + 2*self.S2
		self.start_time = time.clock()
		self.steps_for_speed = 0
		self.distance = 0
		encoders.connected_encoders.append(self)
	def fsm(self,old,new):
		TABLE = [0,-1,1,0,
				1,0,0,-1,
				-1,0,0,1,
				0,1,-1,0]
		return TABLE[4*old+new]       
	
	def update(self):
		#correponding C pin to output
		#corresponding C pin to HIGH
		RPIO.setup(self.c, RPIO.OUT)
		RPIO.output(self.c, True)
		time.sleep(0.005)
		self.newS1 = RPIO.input(encoders.a)
		self.newS2 = RPIO.input(encoders.b)
		RPIO.setup(self.c, RPIO.IN)
		#after reading, go back to high impedance, should check if this is pull-down or at least floating
		self.new_state = self.newS1 + 2*self.newS2 		
		self.rotation = self.fsm(self.state,self.new_state) #checks if the state is different from before
		self.distance+=self.rotation
		if time.clock()-encoder.DEL_TIME>self.start_time:
			self.speed = self.steps_for_speed/encoder.DEL_TIME
			self.steps_for_speed = 0
			self.start_time = time.clock()
		else: 
			self.steps_for_speed += self.rotation

	def get_speed(self):
		return self.speed
	def get_dist(self):
		return self.distance

