from hardware import imu




x = imu.IMU_device(0x19,0x1e,0x6b)

time.sleep(1)

print x.accel.read()
print x.gyro.read()
print x.comp.read()




