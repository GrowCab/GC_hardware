import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program
  
class DV1910e:
	def __init__(self, speed_pin=12, switch_pin=13):
		self.speed_pin  = speed_pin
		self.switch_pin = switch_pin
#		IO.setwarnings(False)           #do not show any warnings
		IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
		self.pin = IO.setup(speed_pin, IO.OUT)           # initialize GPIO19 as an output.
		self.speed(1)

	def speed(self, speed = 1):
		#range of hz: 1khz-10khz (1 to 10 as the input)
		if(speed == 0):
			hz = 300
		else:
			hz = speed * 1000
		#hz = speed
		print(hz)
		p = IO.PWM(self.speed_pin, hz)          #GPIO19 as PWM output, with 100Hz frequency


if __name__ == '__main__': 
	cooling = DV1910e(speed_pin=13)
	while 1:                               #execute loop forever
		for x in range (1000):     
			                     #execute loop for 50 times, x being incremented from 0 to 49.
			print("Setting pump to " +str(x))
			cooling.speed(x+1)               #change duty cycle for varying the brightness of LED.
			time.sleep(5)                           #sleep for 100m second







