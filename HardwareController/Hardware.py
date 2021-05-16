from abc import ABC, abstractmethod, abstractproperty
import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI

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

class Switch(Actuator):
		
	def on(self):
		GPIO.output(self.control_pin, GPIO.HIGH)
		self.status = True

	def off(self):
		GPIO.output(self.control_pin, GPIO.LOW)
		self.status = False 
	
	@property
	def control_pin(self):
		return self.__pin
	
	@control_pin.setter
	def control_pin(self, value):
		self.__pin = value
		if hasattr(self, '__pin'):
			raise ValueError("control_pin can only be set once")
		self.__pin = value
		GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
		GPIO.setup(self.__pin, GPIO.OUT)  
		self.off()

	def status(self):
		return self.status

class Measurement():
	__slots__ = 'unit', 'value', 'type', 'timestamp'
	def __str__(self):
		return  str(self.timestamp)  + " : " + str(self.value) + " " + self.unit 
