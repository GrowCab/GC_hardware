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
		if self.status != SwitchStatus.ON or self.force:
			if self.gpio:
				GPIO.output(self.control_pin, GPIO.HIGH)
			else:
				# print("Multi rely ON")
				self.multi_relay.turn_on_channel(self.control_pin)
			self.status = SwitchStatus.ON
			self.last_change = datetime.now()

	def off(self):
		if self.status != SwitchStatus.OFF or self.force:
			if self.gpio:
				GPIO.output(self.control_pin, GPIO.LOW)
			else:
				#print("Multi rely OFF")
				self.multi_relay.turn_off_channel(self.control_pin)
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
		
		if self.gpio:
			print("SETTING BCM pin")
			GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
			GPIO.setup(self.__pin, GPIO.OUT) 
		# else: 
		# 	print("We are using multi_relay!!!!!!!!!!!____")

		# if hasattr(self, "__relay"):
		# 	print("Control pin, we are using the multi relay")
		# 	self.gpio = False
		# else:
		# 	print("SETTING BCM pin")
		# 	GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
		# 	GPIO.setup(self.__pin, GPIO.OUT) 
		# 	self.gpio = True 
		self.off()

	@property
	def multi_relay(self):
		return self.__relay

	@multi_relay.setter
	def multi_relay(self, value):
		print("Setting multi_relay")
		self.gpio = False
		self.__relay = value
		if hasattr(self, '__pin'):
			delattr(self, '__pin')

	def status(self):
		return self.status
