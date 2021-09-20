from HardwareController.Hardware  import Sensor, Measurement
from HardwareController.I2C_tools import I2C

from smbus2 import SMBus
import bme280

class BME280(I2C):
#Documentation of the sensor: https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf 

	def __init__(self, address=0x76, bus=None):
		self.setup(address=address, bus=bus)

	def calibrate(self):
		return bme280.load_calibration_params(self.bus, self.address)

	def measure(self, property):
		data = bme280.sample(self.bus, self.address, self.calibration)
		#print(data.id)
		measurement = Measurement()
		measurement.timestamp = data.timestamp
		measurement.type = property
		if measurement.type   == "temperature":
			measurement.value = data.temperature
			measurement.unit  = "C"
		elif measurement.type == "pressure":
			measurement.value = data.pressure
			measurement.unit  = "Bar"
		elif measurement.type == "humidity":
			measurement.value = data.humidity
			measurement.unit  = "%"
		else:
			raise NotImplementedError
		return measurement

	def measures(self):
		return ["temperature", "pressure", "humidity"]

	def __str__(self):
		return "BME280"


if __name__ == '__main__':
	bme = BME280(bus=SMBus(1))
	print("Measures: ")
	print(bme.measures())
	print(bme.measure("temperature"))
	print(bme.measure("humidity"))
	print(bme.measure("pressure"))

