import RPi.GPIO as gpio
import time
import Adafruit_DHT

class Sensors():
	def __init__(self, gpio_pir: int, gpio_microphone: int, dht_11_temp: int):
		gpio.setmode(gpio.BOARD)
		
		gpio.setup(gpio_pir, gpio.IN)
		gpio.setup(gpio_microphone, gpio.IN)
		print("wait 5 seconds for sensors to settle")
		time.sleep(5)
		
		self.gpio_pir = gpio_pir
		self.gpio_microphone = gpio_microphone
		self.dht_11_temp = dht_11_temp
		self.dht_11_sensor = Adafruit_DHT.DHT11
		self.event_callbacks_setup = False

	def setup_event_callbacks(self, callback: callable, callback_args: list):
		if self.event_callbacks_setup:
			print("callbacks already set up, skipping")
		else:
			gpio.add_event_detect(self.gpio_microphone, gpio.RISING, callback=lambda channel: callback(*callback_args), bouncetime=1000)
			gpio.add_event_detect(self.gpio_pir, gpio.RISING, callback=lambda channel: callback(*callback_args), bouncetime=1000)
	 
	def detect(self) -> bool:
		_, temperature = Adafruit_DHT.read_retry(self.dht_11_sensor, self.dht_11_temp)
		print(f"current temperature: {temperature}")
		if gpio.input(self.gpio_microphone):
			print("microphone detection!!")
			return True
		if gpio.input(self.gpio_pir):
			print("pir detection!")
			return True
		return False
		
	
