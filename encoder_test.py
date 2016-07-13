import encoder
import time


component_measure = encoder.encoders(20,21) #pins A and B
component    =    component_measure.encoder(16) #pin C


c=0
while true:
	component_measure.update()
	sleep(0.01)
	c+=1
	if c > 500:
		c=0
		print component.get_dist() 
	pass







