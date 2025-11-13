import RPi.GPIO as gpio
import time
class Sensors():
	def __init__(self, gpio_pir_1: int, gpio_pir_2: int, gpio_microphone: int):
		gpio.setmode(gpio.BOARD)
		
		gpio.setup(gpio_pir_1, gpio.IN)
		gpio.setup(gpio_pir_2, gpio.IN)
		gpio.setup(gpio_microphone, gpio.IN)
		print("wait 5 seconds for sensors to settle")
		time.sleep(5)
		
		self.gpio_pir_1 = gpio_pir_1
		self.gpio_pir_2 = gpio_pir_2
		self.gpio_microphone = gpio_microphone
		self.event_callbacks_setup = False

	def setup_event_callbacks(self, callback: callable):
		if self.event_callbacks_setup:
			print("callbacks already set up, skipping")
		else:
			gpio.add_event_detect(self.gpio_microphone, gpio.RISING, callback, bouncetime=1000)
			gpio.add_event_detect(self.gpio_pir_1, gpio.RISING, callback, bouncetime=1000)
			gpio.add_event_detect(self.gpio_pir_2, gpio.RISING, callback, bouncetime=1000)
	
	def detect(self) -> bool:
		if gpio.input(self.gpio_pir_1):
			print("pir 1 detection!")
			return True
		if gpio.input(self.gpio_pir_2):
			print("pir 2 detection!")
			return True
		if gpio.input(self.gpio_microphone):
			print("microphone detection!!")
			return True
		return False
		
	
