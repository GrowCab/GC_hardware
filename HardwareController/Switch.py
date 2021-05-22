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