
#install the stuff needed
#sudo nano /etc/modprobe.d/raspi-blacklist.conf
	#unblacklist the i2c
#sudo echo "i2c-dev" >> /etc/modules
#sudo apt-get update
#sudo apt-get install i2c-tools
#sudo apt-get install python-smbus
#sudo adduser pi i2c
#sudo reboot

#test if you have installed all of it
#i2cdetect -y 1 #the bus in the pi is #1, zero doesn't exist

import smbus
#import time
#0x19 & 0x1E & 0x6B
#address = 0xAA # check to see the addresses of each module of the imu
#bus.read_byte_data(address_to_device, register) #register is read as cmd in the smbus files
class IMU_device:
	bus = smbus.SMBus(1) #the bus is global if something else accesses the i2c, maybe there'll be a problem
	def __init__(self,accel_address,gyro_address,comp_address):
		self.accel = IMU_accel(accel_address)
		self.gyro  = IMU_gyro(gyro_address)
		self.comp  = IMU_comp(comp_address)

class IMU_accel(IMU_device):
	def __init__(self,device_address):
		self.address = device_address
		IMU_device.bus.write_byte_data(self.address,0x20, 0x27) #enables the accel writing to first control register, 10Hz data

	def read(self):
		def data_convert(number):
		#converts a 2 byte number into a signed one
			sig = number & ( 0x8000)
			mag = number & (~0x8000)#the operator ~ in python does ~n => -n-1
			return -sig+mag
		x  = IMU_device.bus.read_byte_data(self.address, 0x29) << 8 #read and shift to MSB
		x |= IMU_device.bus.read_byte_data(self.address, 0x28)      #read LSB and combine with previous

		y  = IMU_device.bus.read_byte_data(self.address, 0x2B) << 8 #read and shift to MSB
		y |= IMU_device.bus.read_byte_data(self.address, 0x2A)      #read LSB and combine with previous

		z  = IMU_device.bus.read_byte_data(self.address, 0x2D) << 8 #read and shift to MSB
		z |= IMU_device.bus.read_byte_data(self.address, 0x2C)      #read LSB and combine with previous
		return [data_convert(x),data_convert(y),data_convert(z)]

class IMU_gyro(IMU_device):
	def __init__(self,device_address):
		self.address = device_address
		IMU_device.bus.write_byte_data(self.address,0x20, 0xbf) #enables the accel writing to first control register, 10Hz data

	def read(self):
		def data_convert(number):
		#converts a 2 byte number into a signed one
			sig = number & ( 0x8000)
			mag = number & (~0x8000)#the operator ~ in python does ~n => -n-1
			return -sig+mag
		x  = IMU_device.bus.read_byte_data(self.address, 0x29) << 8 #read and shift to MSB
		x |= IMU_device.bus.read_byte_data(self.address, 0x28)      #read LSB and combine with previous

		y  = IMU_device.bus.read_byte_data(self.address, 0x2B) << 8 #read and shift to MSB
		y |= IMU_device.bus.read_byte_data(self.address, 0x2A)      #read LSB and combine with previous

		z  = IMU_device.bus.read_byte_data(self.address, 0x2D) << 8 #read and shift to MSB
		z |= IMU_device.bus.read_byte_data(self.address, 0x2C)      #read LSB and combine with previous
		return [data_convert(x),data_convert(y),data_convert(z)]

class IMU_comp(IMU_device):
	def __init__(self,device_address):
		self.address = device_address
		IMU_device.bus.write_byte_data(self.address,0x02, 0x00)
		IMU_device.bus.write_byte_data(self.address,0x01, 0x20)

	def read(self):
		def data_convert(number):
		#converts a 2 byte number into a signed one
			sig = number & ( 0x8000)
			mag = number & (~0x8000)#the operator ~ in python does ~n => -n-1
			return -sig+mag
		x  = IMU_device.bus.read_byte_data(self.address, 0x04) << 8 #read and shift to MSB
		x |= IMU_device.bus.read_byte_data(self.address, 0x03)      #read LSB and combine with previous

		y  = IMU_device.bus.read_byte_data(self.address, 0x06) << 8 #read and shift to MSB
		y |= IMU_device.bus.read_byte_data(self.address, 0x05)      #read LSB and combine with previous

		z  = IMU_device.bus.read_byte_data(self.address, 0x08) << 8 #read and shift to MSB
		z |= IMU_device.bus.read_byte_data(self.address, 0x07)      #read LSB and combine with previous
		return [data_convert(x),data_convert(y),data_convert(z)]

