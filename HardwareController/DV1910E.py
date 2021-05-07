import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program
  
class DV1910e:
	def __init__(self, speed_pin=12, switch_pin=16):
		self.speed_pin  = speed_pin
		self.switch_pin = switch_pin
		GPIO.setwarnings(True)           #do not show any warnings
		GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
		GPIO.setup(speed_pin, GPIO.OUT)           # initialize GPIO12 as an output.
		self.p = GPIO.PWM(self.speed_pin, 50)

		GPIO.setup(self.switch_pin, GPIO.OUT)
		#self.p.ChangeDutyCycle(95) 
		self.p.start(99)
		# while 1:
		# 	for dc in range(0, 101, 5):
		# 		self.p.ChangeDutyCycle(dc)
		# 		time.sleep(0.1)
		# 	for dc in range(100, -1, -5):
		# 		self.p.ChangeDutyCycle(dc)
		# 		time.sleep(0.1)

		
		


	def speed(self, speed = 1):
		#range of hz: 1khz-10khz (1 to 10 as the input)
		hz = 0
		if(speed == 0):
			hz = 300
		else:
			hz = speed * 1000
		hz = speed
		print(hz)
		self.p.ChangeFrequency(hz)
		if speed % 2:
			print("ON")
			GPIO.output(self.switch_pin, GPIO.HIGH)
		else:
			print("OFF")
			GPIO.output(self.switch_pin, GPIO.LOW)
		#
		#p = GPIO.PWM(self.speed_pin, hz)          #GPIO19 as PWM output, with 100Hz frequency
		#GPIO.output(self.speed_pin, GPIO.HIGH)
		#p.start


if __name__ == '__main__': 
	cooling = DV1910e(speed_pin=12)
	while 1:                               #execute loop forever
		for x in range (10):
			print("Setting pump to " +str(5))
			#GPIO.output(12, GPIO.HIGH)
			#cooling.speed(x+1)               #change duty cycle for varying the brightness of LED.
			
			cooling.speed(5) 
			time.sleep(60)                           #sleep for 100m second







