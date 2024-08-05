import esp
esp.osdebug(0)

import machine
import urequests
import network
from machine import Pin, SoftI2C
from time import sleep, time
from dht import DHT11
from package.lcd_api import LcdApi
from package.i2c_lcd import I2cLcd

THINGSPEAK_WRITE_API_KEY = '4VCJNWLFN8K767PB'
WIFI_SSID = 'Lau_2_a'
WIFI_PASSWORD = 'A1234567893a1'
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

data = DHT11(Pin(4))
i2c = SoftI2C(scl=Pin(9), sda=Pin(8), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
prev_temp = None
prev_humi = None

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        sleep(1)
    print('Connected to WiFi')
    print('IP address:', wlan.ifconfig()[0])

def send_to_thingspeak(temp, humi):
    url = 'https://api.thingspeak.com/update'
    payload = 'api_key={}&field1={}&field2={}'.format(THINGSPEAK_WRITE_API_KEY, temp, humi)
    
    try:
        response = urequests.post(url, data=payload)
        if response.status_code == 200:
            print('Data sent to ThingSpeak via HTTP successfully')
        else:
            print('Failed to send data to ThingSpeak via HTTP:', response.status_code)
    except Exception as e:
        print('Error sending data to ThingSpeak via HTTP:', e)
    finally:
        response.close()

connect_wifi(WIFI_SSID, WIFI_PASSWORD)

last_send_time = time()
send_interval = 20
start_time = time()

while time() - start_time < 45 * 60:
    try:
        data.measure()
        temp = data.temperature()
        humi = data.humidity()
        if temp != prev_temp:
            lcd.move_to(0, 0)
            lcd.putstr("Temp: {} C".format(temp))
            prev_temp = temp
        if humi != prev_humi:
            lcd.move_to(0, 1)
            lcd.putstr("Humi: {} %".format(humi))
            prev_humi = humi
        if time() - last_send_time >= send_interval:
            send_to_thingspeak(temp, humi)
            last_send_time = time()
        sleep(1)
    except OSError as e:
        lcd.clear()
        lcd.putstr("Failed to read")
        sleep(2)
        lcd.clear()
        sleep(2)
