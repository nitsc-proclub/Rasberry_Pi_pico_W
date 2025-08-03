from picozero import LED        # LED制御用
from time import sleep          # 待ち時間

led1 = LED(5)                   # GP5にLED接続

while True:                     # ずっと繰り返す
    led1.on()                   # 点灯
    sleep(0.5)                  # 0.5秒待つ
    led1.off()                  # 消灯
    sleep(0.5)                  # 0.5秒待つ
