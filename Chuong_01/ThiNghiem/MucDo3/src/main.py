import esp
esp.osdebug(0)
from machine import Pin, PWM
from time import sleep, sleep_us, sleep_ms
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

def check_state(dec, hex):
	if(dec & hex) != 0:
		return True
	return False

count = 0

while True:
	set_level_gpio_output(4, check_state(count, 0x80))
	set_level_gpio_output(5, check_state(count, 0x40))
	set_level_gpio_output(6, check_state(count, 0x20))
	set_level_gpio_output(7, check_state(count, 0x10))
	set_level_gpio_output(15, check_state(count, 0x08))
	set_level_gpio_output(16, check_state(count, 0x04))
	set_level_gpio_output(17, check_state(count, 0x02))
	set_level_gpio_output(18, check_state(count, 0x01))
	sleep(1)
	count += 1
	if count == 256:
		count = 0