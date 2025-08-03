from machine import Pin
import time

interval = 0.1
led1 = Pin(9, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(17 , Pin.OUT)
led4 = Pin(21, Pin.OUT)

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)

while True:
    for i in range(15) :
        led4.value(0)
        led1.value(1)
        time.sleep(interval)
    
        led1.value(0)
        led2.value(1)
        time.sleep(interval)
    
        led2.value(0)
        led3.value(1)
        time.sleep(interval)
    
        led3.value(0)
        led4.value(1)
        time.sleep(interval)
    
    for j in range(5) :
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(1)
        time.sleep(0.3)
        
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        time.sleep(0.3)
        
    
    
    