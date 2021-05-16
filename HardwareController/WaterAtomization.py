from HardwareController.Hardware import Switch
import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program
  
class WaterAtomization(Switch):
	def __init__(self, control_pin):
		self.control_pin = control_pin

	def controls(self):
		return ["humidity"]



if __name__ == '__main__': 
	control_pin = 24
	wa = WaterAtomization(control_pin)
	i = 5
	print(wa.controls());
	while i > 0:
		print(str(i))
		print("On")
		wa.on()
		i -= 1

		time.sleep(5)
		print("Off")
		wa.off()
		time.sleep(5)

	GPIO.cleanup()




