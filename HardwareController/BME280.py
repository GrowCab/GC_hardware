from Hardware  import Sensor, Meassurment
from I2C_tools import I2C

import smbus2
import bme280
#Documentation of the sensor: https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf 
class BME280(Sensor):
	__slots__ = 'address', 'port', 'bus'

	def __init__(self, address=0x76, port=1):
		self.address = address
		self.port    = port
		self.__online = self.is_online(reconnect=True)
		self.bus   = smbus2.SMBus(port)
		self.__calibration = bme280.load_calibration_params(self.bus, self.address)

	def is_online(self, reconnect=False):
		if(reconnect):
			addr = I2C.scan()
			self.__online = self.address in addr
		return self.__online

	def measure(self, property):
		data = bme280.sample(self.bus, self.address, self.__calibration)
		#print(data.id)
		messurment = Meassurment()
		messurment.timestamp = data.timestamp
		messurment.type = property
		if messurment.type == "temperature":
			messurment.value = data.temperature
			messurment.unit  = "C"
		elif messurment.type == "pressure":
			messurment.value = data.pressure
			messurment.unit  = "Bar"
		elif messurment.type == "humidity":
			messurment.value = data.humidity
			messurment.unit  = "%"
		else:
			raise NotImplementedError

		#print(data.temperature)
		#print(data.pressure)
		#print(data.humidity)
		
		#messurment.type  = 'temperature'
		return messurment

#print(data.timestamp)
#print(data.temperature)
#print(data.pressure)
#print(data.humidity)
		#raise NotImplementedError

	def measures(self):
		return ["temperature", "pressure", "humidity"]


if __name__ == '__main__':
	bme = BME280()
	print("Measuers: ")
	print(bme.measures())
	print(bme.measure("temperature"))
	print(bme.measure("humidity"))
	print(bme.measure("pressure"))

