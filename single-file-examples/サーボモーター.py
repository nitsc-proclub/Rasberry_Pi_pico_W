from picozero import Servo   # サーボ用
from time import sleep       # 待ち時間

servo = Servo(0, None, 0.0005, 0.0024)  # GP0に接続して初期化

while True:                  # ずっと繰り返す
    servo.value = 45 / 90   # サーボを45°に動かす
    sleep(0.5)              # 0.5秒待つ
    servo.value = 135 / 90  # サーボを135°に動かす
    sleep(0.5)              # 0.5秒待つ
