import hardware.encoder as encoder
import hardware.esc     as esc
import hardware.motor   as motor
import hardware.imu     as imu
import thread
import re

#setup:
component_measure = encoder.encoders(20,21) #pins A and B
component    =  encoder.encoder(16) #pin C

component_measure.update()

mymotor = esc.motor('m1', 17, simulation=False)
mymotor.start()
mymotor.setW(0)

x = imu.IMU_device(0x19,0x6b,0x1e)  #remember to connect the imu, 
												#addresses are fixed
mot1     = motor.motor()

driver1  = mot1.driver()
driver1.add_motor(16,19)#put the right pins for each of the motors
driver1.add_motor(16,19)

driver2  = mot1.driver()
driver2.add_motor(16,19)
driver1.add_motor(16,19)

#loop:
run = True
while run:
	print "commands are: move dist angle; brush duty; imu; encoder; exit;"
	command = raw_input()
	match = re.search(r"\Amove (\d*) (\d*)", command)
	if(match):
		print "doing: move ",match.group(1),match.group(2) #remember these groups are strings, use Int(group_a) to convert them to ints
		pass
	match = re.search(r"\Abrush (\d*)", command)
	if(match):
		print "doing: brush ",match.group(1)
		pass
	match = re.search(r"\Aimu", command)
	if(match):
		print "doing: imu "
		pass
	match = re.search(r"\Aencoder", command)
	if(match):
		print "doing: encoder "
		pass
	match = re.search(r"\Aexit", command)
	if(match):
		run = False #ends the loop
		pass

