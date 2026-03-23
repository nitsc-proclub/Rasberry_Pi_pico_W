# 無線接続
from wifi import run  # wifi.pyからrun関数をインポート

SSID = ''  # Wi-FiのSSID
PASSWORD = ''  # Wi-Fiのパスワード

html = """
<!doctype html>
<h1>Hello World</h1>
"""  # HTMLの内容

run(SSID, PASSWORD, html)  # Wi-Fiに接続してWebサーバを起動