import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program
  
class WaterAtomization:
	def __init__(self, control_pin=24):
		self.control_pin  = control_pin
		GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
		GPIO.setup(control_pin, GPIO.OUT)  

	def on(self):
		GPIO.output(self.control_pin, GPIO.HIGH)

	def off(self):
		GPIO.output(self.control_pin, GPIO.LOW)




if __name__ == '__main__': 
	wa = WaterAtomization(control_pin=24)
	i = 5
	while i > 0:
		print(str(i))
		print("On")
		wa.on()
		i -= 1

		time.sleep(5)
#		print("Off")
		#wa.off()
		time.sleep(5)

	GPIO.cleanup()




