import esp
esp.osdebug(0)
from machine import Pin, PWM
from time import sleep
from sys import exit

def set_level_gpio_output(gpio, state):
	if not ((1 <= gpio <= 21) or (35 <= gpio <= 45) or gpio in [47, 48]):
		print("Hãy nhập GPIO NUMBER từ 1 - 21, 35 - 45, 47, 48")
		exit()
	if state not in (0, 1, False, True):
		print("Hãy nhập GPIO LEVEL là 0 (False) và 1 (True)")
		exit()
	gpio_t = Pin(gpio, Pin.OUT)
	if state in (0, False):
		gpio_t.value(1)
	elif state in (1, True):
		gpio_t.value(0)

while True:
	set_level_gpio_output(4, True)
	sleep(1)
	set_level_gpio_output(4, False)
	sleep(3)