from picozero import Button        # 照度センサ→Button扱い
from time import sleep             # 待ち時間

light = Button(15, pull_up=True)   # GP15に照度センサの片足を接続（もう片足はGND）

while True:                        # ずっと繰り返す
    if light.is_pressed: print("明るい") # もし 明るかったら「明るい」と表示
    else: print("暗い")                  # そうでなければ（暗かったら）「暗い」と表示
    sleep(0.1)                     # 0.1秒待つ