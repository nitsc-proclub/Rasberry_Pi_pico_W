#無線接続
from wifi import run                    # wifi.pyからrun関数をインポート

SSID = 'Mamoru'                         # Wi-FiのSSID
PASSWORD = 'twux3602'                   # Wi-Fiのパスワード

html = """
<!doctype html>
<h1>Hello World</h1>
"""                                     # HTMLの内容

run(SSID, PASSWORD, html)               # Wi-Fiに接続してWebサーバを起動