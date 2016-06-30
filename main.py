import RPIO
import threading
import encoder
import imu
import esc
import motor

def wheelsFunction():




def main():
	my_imu = IMU_device(0x19,0x1E,0x6B)#their order might be wrong, check later
	#also, if more wheels, create more encoder objs, so each is measured by one
	my_encoder1 = encoder(0,0,0)#find the real pins the encoder will be attached to
	my_encoder2 = encoder(0,0,0)#find the real pins the encoder will be attached to
	
	#this will keep checking the encoders for position change
	#should we worry about debouncing the encoder?
	encoder_thread1 =  threading.Thread(target=my_encoder1.update)
	encoder_thread2 =  threading.Thread(target=my_encoder2.update)
	encoder_thread1.start()
	encoder_thread2.start()


	wheels= threading.Thread(target=wheelsFunction)



if __name__ == "__main__":
    main()

