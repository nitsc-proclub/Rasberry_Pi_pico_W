from picozero import Servo   # サーボ用
from time import sleep       # 待ち時間

servo = Servo(0)             # GP0に接続して初期化

while True:                  # ずっと繰り返す
    servo.value = 0 / 90   # サーボを0°に動かす
    sleep(0.5)              # 0.5秒待つ
    servo.value = 90 / 90  # サーボを90°に動かす
    sleep(0.5)              # 0.5秒待つ
