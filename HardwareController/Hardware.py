from abc import ABC, abstractmethod, abstractproperty

class Sensor(ABC):
	@abstractmethod
	def measure(self, unit):
		pass

	@abstractmethod
	def measures(self):
		pass

	@abstractmethod
	def is_online(self):
		pass

	def can_measure(self, property):
		return property in self.measures()

class Actuator(ABC):

	@abstractmethod
	def controls(self):
		pass



class Meassurment():
	__slots__ = 'unit', 'value', 'type', 'timestamp'

	def __str__(self):
		return  str(self.timestamp)  + " : " + str(self.value) + " " + self.unit 
