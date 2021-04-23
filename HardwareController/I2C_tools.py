from smbus2 import SMBus
from .Hardware  import Sensor, Meassurment
from abc import ABC, abstractmethod, abstractproperty


class I2C(Sensor):

	def is_online(self, reconnect=False):
		if(reconnect):
			addr = I2C.scan(port=self.port)
			self.__online = self.address in addr
		return self.__online

	def setup(self, address=None, port=None):
		if address == None or port == None:
			raise NotImplementedError
		self.address = address
		self.port    = port
		self.__online = self.is_online(reconnect=True)
		self.bus   = SMBus(port)
		self.__calibration = self.calibrate()

	@property
	def calibration(self):
		return self.__calibration

	#@abstractmethod
	def calibrate(self):
		raise NotImplementedError

	#Based on the code from https://gist.github.com/kungpfui/54784ebc3b3ca72169c1839720b313bf 
	def scan(force=False, port=1):
		devices = []
		for addr in range(0x03, 0x77 + 1):
			read = SMBus.read_byte, (addr,), {'force':force}
			write = SMBus.write_byte, (addr, 0), {'force':force}

			for func, args, kwargs in (read, write):
				try:
					with SMBus(port) as bus:
						data = func(bus, *args, **kwargs)
						devices.append(addr)
						break
				except OSError as expt:
					if expt.errno == 16:
						# just busy, maybe permanent by a kernel driver or just temporary by some user code
						pass
		return devices
 



if __name__ == '__main__':
	for addr in I2C.scan(force=True):
		print('{:02X}'.format(addr))