import encoder
import time


component_measure = encoder.encoders(20,21) #pins A and B
print encoder.encoders.a
print component_measure.b
component    =  encoder.encoder(16) #pin C
acc_state = 0

c=0
cont = 0
while True:
	component_measure.update()
	time.sleep(0.01)
	if acc_state != component.new_state:
		acc_state = component.new_state
		#print acc_state
		cont +=1
	c+=1
	if c > 200:
		c=0
		print cont
		#print '>>>>>>',component.get_dist() 
	pass







