from Hardware  import Sensor, Meassurment
from I2C_tools import I2C

from smbus2 import SMBus
import bme280

class BME280(I2C):
	__slots__ = 'address', 'port', 'bus'

	def __init__(self, address=0x76, port=1):
		self.setup(address=address, port=port)

	def calibrate(self):
		return bme280.load_calibration_params(self.bus, self.address)

	def measure(self, property):
		data = bme280.sample(self.bus, self.address, self.calibration)
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
		return messurment

	def measures(self):
		return ["temperature", "pressure", "humidity"]


if __name__ == '__main__':
	bme = BME280()
	print("Measuers: ")
	print(bme.measures())
	print(bme.measure("temperature"))
	print(bme.measure("humidity"))
	print(bme.measure("pressure"))

