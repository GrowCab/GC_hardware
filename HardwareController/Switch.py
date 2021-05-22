from HardwareController.Hardware import Actuator
from copy import Error
from enum import Enum
from datetime import datetime
import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI

class SwitchStatus(Enum):
	ON  = True
	OFF = False

class Switch(Actuator):
		
	def on(self):
		if self.status != SwitchStatus.ON:
			GPIO.output(self.control_pin, GPIO.HIGH)
			self.status = SwitchStatus.ON
			self.last_change = datetime.now()

	def off(self):
		if self.status != SwitchStatus.OFF :
			GPIO.output(self.control_pin, GPIO.LOW)
			self.status = SwitchStatus.OFF
			self.last_change = datetime.now()

	def turn(self, switch_status):
		if switch_status == SwitchStatus.ON:
			self.on()
		elif switch_status == SwitchStatus.OFF:
			self.off()
		else:
			raise Error("Invalid switch status")

	
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

	