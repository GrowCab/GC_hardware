from abc import ABC, abstractmethod, abstractproperty

class Measurement():
	__slots__ = 'unit', 'value', 'type', 'timestamp'
	def __str__(self):
		return  str(self.timestamp)  + " : " + str(self.value) + " " + self.unit 


class Sensor(ABC):
	@abstractmethod
	def measure(self, unit) -> Measurement:
		pass

	@abstractmethod
	def measures(self) -> str:
		pass

	@abstractmethod
	def is_online(self) -> bool:
		pass

	def can_measure(self, property) -> bool:
		return property in self.measures()


class Actuator(ABC):

	@abstractmethod
	def controls(self) -> str:
		pass

	@property
	def expected_status(self):
		return self.__expected_status

	@expected_status.setter
	def expected_status(self, value):
		self.__expected_status = value
		if self.__expected_status != None:
			self.checkAndActuate(value)

	@abstractmethod
	def checkAndActuate(self, value) -> None:
		pass

	@property
	def force(self) -> bool:
		return self.__force
		
	@force.setter
	def force(self, value):
		self.__force = value