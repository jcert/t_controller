from hardware import imu
import time



x = imu.IMU_device(0x19,0x6b,0x1e)



for i in range(0,20):
	time.sleep(0.3)
	print "a",x.accel.read()
	print "g",x.gyro.read()
	print "c",x.comp.read()
	print "_____"




