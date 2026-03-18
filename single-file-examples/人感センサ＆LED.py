from picozero import Button
from picozero import LED
from time import sleep

# GP0 に PIR の OUT を接続
light = Button(0, pull_up=True)

# GP5 に LED を接続
led1 = LED(5)

while True:
    if light.is_pressed:
        print("非検知")
        led1.off()
    else:
        print("検知")
        led1.on()
    sleep(0.1)
