
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
#i2cdetect -y 0

import smbus
import time
#0x19 & 0x1E & 0x6B
#address = 0xAA # check to see the addresses of each module of the imu
#bus.read_byte_data(address_to_device, register) #register is read as cmd in the smbus files
class IMU_device:
		bus = smbus.SMBus(0) #the bus is global if something else accesses the i2c, maybe there'll be a problem
	def __init__(self,accel_address,gyro_address,comp_address):
		self.accel = IMU_accel(accel_address)
		self.gyro  = IMU_gyro(gyro_address)
		self.comp  = IMU_comp(comp_address)

class IMU_accel:
	def __init__(self,device_address):
		self.address = device_address

	def read(self):
		self.x  = bus.read_byte_data(self.address, 0x29) << 8 #read and shift to MSB
		self.x |= bus.read_byte_data(self.address, 0x28)      #read LSB and combine with previous

		self.y  = bus.read_byte_data(self.address, 0x2B) << 8 #read and shift to MSB
		self.y |= bus.read_byte_data(self.address, 0x2A)      #read LSB and combine with previous

		self.z  = bus.read_byte_data(self.address, 0x2D) << 8 #read and shift to MSB
		self.z |= bus.read_byte_data(self.address, 0x2C)      #read LSB and combine with previous
		return [x,y,z]

class IMU_gyro:
	def __init__(self,device_address):
		self.address = device_address

	def read(self):
		self.x  = bus.read_byte_data(self.address, 0x29) << 8 #read and shift to MSB
		self.x |= bus.read_byte_data(self.address, 0x28)      #read LSB and combine with previous

		self.y  = bus.read_byte_data(self.address, 0x2B) << 8 #read and shift to MSB
		self.y |= bus.read_byte_data(self.address, 0x2A)      #read LSB and combine with previous

		self.z  = bus.read_byte_data(self.address, 0x2D) << 8 #read and shift to MSB
		self.z |= bus.read_byte_data(self.address, 0x2C)      #read LSB and combine with previous
		return [x,y,z]

class IMU_comp:
	def __init__(self,device_address):
		self.address = device_address

	def read(self):
		self.x  = bus.read_byte_data(self.address, 0x04) << 8 #read and shift to MSB
		self.x |= bus.read_byte_data(self.address, 0x03)      #read LSB and combine with previous

		self.y  = bus.read_byte_data(self.address, 0x06) << 8 #read and shift to MSB
		self.y |= bus.read_byte_data(self.address, 0x05)      #read LSB and combine with previous

		self.z  = bus.read_byte_data(self.address, 0x08) << 8 #read and shift to MSB
		self.z |= bus.read_byte_data(self.address, 0x07)      #read LSB and combine with previous
		return [x,y,z]

