import esp
esp.osdebug(0)
from machine import Pin, PWM
from time import sleep, sleep_us, sleep_ms
from sys import exit

def set_level_gpio_output(gpio, state):
	# state with 0: ON, 1: OFF
	if not ((1 <= gpio <= 21) or (35 <= gpio <= 45) or gpio in [47, 48]):
		print("Hãy nhập GPIO NUMBER từ 1 - 21, 35 - 45, 47, 48")
		exit()
	if state not in (0, 1):
		print("Hãy nhập GPIO LEVEL là 0 (False) và 1 (True)")
		exit()
	gpio_t = Pin(gpio, Pin.OUT)
	if state in (0, 1):
		gpio_t.value(state) 

def check_state(count, dec):
	if(count & dec):
		return 0
	return 1

count = 15

print("Nhóm 3, 8")

while True:
	set_level_gpio_output(4, check_state(count, 1))
	set_level_gpio_output(5, check_state(count, 2))
	set_level_gpio_output(6, check_state(count, 4))
	set_level_gpio_output(7, check_state(count, 8))
	set_level_gpio_output(15, check_state(count, 8))
	set_level_gpio_output(16, check_state(count, 4))
	set_level_gpio_output(17, check_state(count, 2))
	set_level_gpio_output(18, check_state(count, 1))
	print(f"{check_state(count, 1)} {check_state(count, 2)} {check_state(count, 4)} {check_state(count, 8)} {check_state(count, 8)} {check_state(count, 4)} {check_state(count, 2)} {check_state(count, 1)}")
	sleep(1)
	count -= 1
	if count < 0:
		print("END")
		count = 15