from enum import Enum
from os import O_NOFOLLOW
from pprint import pprint
from typing import Tuple, Union
from HardwareController.Switch import Switch, SwitchStatus
class SwitchEffect(Enum):
	INCREASE = 1
	DECREASE = 2
	ONOFF    = 3

class RangeValues:
	__slots__ = 'trigger', 'stop', 'effect'
	
	def inRange(self, value):
		if self.effect == SwitchEffect.INCREASE:
			return  self.trigger <= value <= self.stop
		elif self.effect == SwitchEffect.INCREASE:
			return  self.stop <= value <= self.trigger
		elif self.effect == SwitchEffect.ONOFF:
			return value == self.trigger

class RangeSwitch(Switch):
	
	def __init__(self, range: 0.5, effect: SwitchEffect.DECREASE, hardware_label='temperature', control_pin = 24, multi_relay=None) -> None:
		super().__init__()
		self.range  = range
		self.effect = effect
		self.hardware_label   = hardware_label
		self.multi_relay = multi_relay
		self.control_pin = control_pin
		self.expected_status = None
		self.force = False

	def controls(self):
		return self.hardware_label

	def thresholds(self) -> RangeValues:
		expected_value = self.expected_status
		if expected_value == None:
			raise Exception(f"Expected value hasn't been set for {self}")
		rv = RangeValues()
		rv.effect = self.effect

		if self.effect == SwitchEffect.ONOFF:
			rv.trigger =  SwitchStatus.ON if expected_value else SwitchStatus.OFF
		if self.effect == SwitchEffect.DECREASE:
			rv.trigger = expected_value + self.range
			rv.stop    = expected_value - self.range
		if self.effect == SwitchEffect.INCREASE:
			rv.trigger = expected_value - self.range
			rv.stop    = expected_value + self.range
		return rv	

	def checkAndActuate(self, value):
		thresholds = self.thresholds()
		#print(f'e:{self.expected_status} v:{value}')
		if self.effect == SwitchEffect.ONOFF:
			value = SwitchStatus.ON if value else SwitchStatus.OFF
			#print(f"ONOFF: {value}")
			self.turn(value)
			return
		if thresholds.inRange(value):
			#print(f"{value} is in the range")
			return 	
		if self.effect == SwitchEffect.INCREASE: 
			#print(f"INCREASE")
			if value < thresholds.trigger:
				self.on()
			if value > thresholds.stop:
				self.off()
		if self.effect == SwitchEffect.DECREASE: 
			#print(f"DECREASE")
			if value > thresholds.trigger:
				self.on()
			if value < thresholds.stop:
				self.off()
	
	def __repr__(self):
		  return f"<RangeSwitch range:{self.range} effect:{self.effect} hardware_label:{self.hardware_label} control_pin:{self.control_pin} expected_status:{self.expected_status}> " 
