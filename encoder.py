import RPIO


class encoder:
	ENCODER_TICKS_TURN = 20
	#pins of the encoder
	A = 0 
	B = 0 
	C = 0
	state=0
	distance=0
	velocity=0
	def __init__(self,pinA, pinB, pinC):
		A = pinA
		B = pinB
		C = pinC
		RPIO.setup(7, RPIO.IN, pull_up_down=RPIO.PUD_UP)
		S1 = GPIO.input(A)
		S2 = GPIO.input(B)
		state = S1 + 2*S2
	   
	def fsm(old,new):
		table = [0,-1,1,0,
	            1,0,0,-1,
	            -1,0,0,1,
	            01,-1,0]
		return table[4*old+new]       
	
	def update():
		newS1 = RPIO.input(A)
		newS2 = RPIO.input(B)
		new_state = newS1 + 2*newS2 		
		rotation = self.fsm(state,new_state) #checks if the state is different from before
		
		distance+=rotation
		velocity=0 #how to estimate the velocity?

	def get_speed():
		return velocity
	def get_dist():
		return distance



