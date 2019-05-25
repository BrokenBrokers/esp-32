import time
import utime
from machine import Pin
from ntptime.ntptime import settime
from umqttsimple import MQTTClient
import ubinascii
import machine


SERVER = 'DNS-Namen oder IP-Adresse' #MQTT Server Address
#CLIENT_ID = 'EPS32'
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b'ESP_NTP_Zeit'


client = MQTTClient(CLIENT_ID, SERVER)
client.connect()

rtc = machine.RTC()

settime()

led = Pin(2,Pin.OUT)

while True:
    led.value(1)
    t = time.time()
    ntp = utime.localtime()
    
    msg = (b'{} ; {} '.format(ntp,t))
    client.publish(TOPIC, msg)
    print(msg)
    led.value(0)
    time.sleep(2)
