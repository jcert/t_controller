from hardware import imu
import time



x = imu.IMU_device(0x19,0x6b,0x1e)

time.sleep(1)

print x.accel.read()
print x.gyro.read()
print x.comp.read()




