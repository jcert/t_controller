from hardware import imu
import time



x = imu.IMU_device(0x19,0x6b,0x1e)



for i in range(0,20):
	time.sleep(0.3)
	print x.accel.read()
	print x.gyro.read()
	print x.comp.read()




