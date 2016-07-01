import RPIO
import threading
import encoder
import imu
import esc
import motor

def wheelsFunction():
	pass

def main():
	my_imu = IMU_device(0x19,0x1E,0x6B)#their order might be wrong, check later
	#also, if more wheels, create more encoder objs, so each is measured by one
	encoder_group = encoders(pinA,pinB)#obj that handles all encoders
	my_encoder1 = encoder_group.encoder(0)#find the real pins the encoder will be attached to
	my_encoder2 = encoder_group.encoder(0)#find the real pins the encoder will be attached to
	my_encoder3 = encoder_group.encoder(0)#find the real pins the encoder will be attached to
	my_encoder4 = encoder_group.encoder(0)#find the real pins the encoder will be attached to
	
	#this will keep checking the encoders for position change
	#should we worry about debouncing the encoder?
	encoder_thread =  threading.Thread(target=encoder_group.update_loop)
	encoder_thread.start()

	wheels= threading.Thread(target=wheelsFunction)
	while True:
		pass

if __name__ == "__main__":
    main()

