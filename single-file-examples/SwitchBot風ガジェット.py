#Webボタンでサーボを動かす
from wifi import run_button                      # wifi.pyからrun_button関数をインポート
from picozero import Servo                       # サーボを使うためのライブラリ
from time import sleep                           # 待ち時間を入れるための関数

SSID = ''                                  # Wi-FiのSSID
PASSWORD = ''                            # Wi-Fiのパスワード

servo = Servo(0, None, 0.0005, 0.0024)           # GP0にサーボを接続
servo.value = 45 / 180                           # はじめの角度（待機位置）

html = """
<!doctype html>
<button onclick="fetch('/push')">押す</button>
"""                                              # Webページの内容

def push_servo():                                # ボタンが押されたときに呼ばれる処理
	servo.value = 45 / 180                        # 45°へ動かす
	sleep(0.15)                                   # 少し待つ
	servo.value = 135 / 180                       # 135°へ動かす
	sleep(0.25)                                   # 少し待つ
	servo.value = 45 / 180                        # 45°へ戻す

run_button(SSID, PASSWORD, html, push_servo)    # Wi-Fi接続してボタンWebサーバを起動

