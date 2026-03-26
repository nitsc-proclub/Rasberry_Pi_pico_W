# ラズパイ Pico W で「どこでもポチっとIoTスイッチ」

## 準備
 - Raspberry Pi pico W（ラズベリー パイ ピコ ダブリュー）
 - USBケーブル（USBマイクロB端子⇔USB-A端子）
 - パソコン（Thonyインストール済）
1. パソコンでThonyを起動
2. パソコンとラズパイをUSBケーブルで接続
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/cable_connect.png" width="80%" />
3. Thonyでラズパイを使用する設定を行う
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/thony_setting.png" width="80%" />

## プログラムを書こう 
### print文
Thonyでコードを打ち込んで「実行ボタン▶️」を押しましょう。
```python
print("Hello, World!")
```
▶️実行結果  
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/result1.png" width="80%" />
- **`print`は文や数を表示する指示です。**
	 - 文字を表示するときは `"こんにちは"` このように囲います。
     - `print(1+1)` のように書くと、算数の計算もできます。
     - 2つ以上のプログラムを書きたいときは、以下のように改行しましょう。
```python
print(1)
print(2)
```

#### 算数の計算
💡`print`に計算の式を入れて遊んでみましょう。

| 計算 | 記号 |
| ------------- | ------------- |
| たしざん | + |
| ひきざん | - |
| かけざん | * |
| わりざん | / |


#### 例➀
```python
print(6 / 3)
```
<details>
<summary>例➀の実行結果</summary>

```python
2
```
6わる3は2です。
</details><br>

#### 例➁
```python
print(2 * 4)
```
<details>
<summary>例➁の実行結果</summary>

```python
8
```
2かける4は8です。
</details><br>

#### 例➂
```python
print(5 + 4)
```
<details>
<summary>例➂の実行結果</summary>

```python
9
```
5たす4は9です。
</details><br>

**💡応用問題：1年は何秒か計算してみよう！**

ヒント
 - 1年は365日
 - 1日は24時間
 - 1時間は60分
 - 1分は60秒
<details>
<summary>解答</summary>

```python
print(365 * 24 * 60 * 60)
```
実行すると、1年は31536000秒と分かります。
</details><br>

## 回路をつくる準備
#### ブレッドボード
 - 部品を差し込む穴がたくさんある板  
 - 簡単に回路をつくれます
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/breadboard.png" width="30%" />
- ボードの内部で線がつながっています
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/breadboard_line.png" width="70%" />

#### ラズパイをボードに差し込む
画像のように差し込みましょう。

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/breadboard_rasberrypi.png" width="50%" />

## LEDを光らせる
#### LEDとは
 - 発光ダイオード
 - 電気を流すと光ります
 - 足が2本です
   - 足が長い方が＋（プラス）
   - 足が短い方－（マイナス）

### LEDの接続
 - ラズパイの左上から7番目のピンの横に足が長い方を差し込みます
 - ラズパイの左上から8番目に短い方を差し込みます
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/LED_connect.png" width="80%" />

### LEDのプログラム
```python
from picozero import LED        # LED制御用
from time import sleep          # 待ち時間

led1 = LED(5)                   # GP5にLED接続

while True:                     # ずっと繰り返す
    led1.on()                   # 点灯
    sleep(0.5)                  # 0.5秒待つ
    led1.off()                  # 消灯
    sleep(0.5)                  # 0.5秒待つ
```
プログラムを日本語に直すと以下のようになります。
```
LEDを制御する宣言
待ち時間を指定する宣言

GPIO5番ピン(GP05)を使用することをラズパイに伝える

ここから下が無限ループ
    LEDを点灯させる
    0.5秒待つ
    LEDを消灯させる
    0.5秒待つ
```
#### 動作
0.5秒ごとに点灯⇔消灯をくりかえします。

<video src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/videos/LED.mp4?raw=true" width="30%" autoplay loop muted playsinline></video>

### 💡LED：応用問題
LEDの数を増やしてみよう

<image src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/LED_4.png?raw=true" width="45%" autoplay loop muted playsinline></image>

## サーボモーターを動かす
#### サーボモーターとは
 - 回転角度を決められるモーターです。  
 SG90の場合・・・0度から180度の範囲
 - 足が3本です  
 平らな面から見たときに
   - 赤の線が＋（プラス）の電源
   - 黄の線が出力
   - 茶の足が－（マイナス）
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/SG-90.png" width="30%" />

### サーボモーターの接続
ジャンパー線を使って繋げましょう。

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/servo_connect.png" width="65%" />

### サーボモーターのプログラム
```python
from picozero import Servo   # サーボ用
from time import sleep       # 待ち時間

servo = Servo(0, None, 0.0005, 0.0024) # GP0に接続して初期化

while True:                  # ずっと繰り返す
    servo.value = 45 / 180   # サーボを45°に動かす
    sleep(0.5)               # 0.5秒待つ
    servo.value = 135 / 180  # サーボを135°に動かす
    sleep(0.5)               # 0.5秒待つ
```
プログラムを日本語に直すと以下のようになります。
```サーボを制御する宣言
待ち時間を指定する宣言

GPIO0番ピン(GP0)を使用する

ここから下が無限ループ
    サーボを45度に動かす
    0.5秒待つ
    サーボを135度に動かす
    0.5秒待つ
```
#### 動作
0.5秒ごとにモーターが45度⇔135度と動きます。

<video src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/videos/servo.mp4?raw=true" width="80%" autoplay loop muted playsinline></video>

### 💡サーボモーター：応用問題
#### あっちむいてホイを作ってみよう
ヒント
 -  `import random` を最初に書くと「ランダム」が使えます
 
つかいかた
 -  `random.choice([45, 135])`→ 45 か 135 にランダムで決まるという意味

## ラズパイをWi-Fiにつなげる
#### Wi-Fiとは
 - 電波でモノとモノをつなぐ仕組みです。
 - ケーブルを使わない→**無線接続**
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/Wi-Fi.png" width="65%" />

### 無線接続のプログラム
```python
from wifi import run	  # wifi.pyからrun関数をインポート

SSID = ‘’				  # Wi-FiのSSID
PASSWORD = ‘’			  # Wi-Fiのパスワード

html = """
<!doctype html>
<h1>Hello World</h1>
"""                  	  # HTMLの内容

run(SSID, PASSWORD, html) # Wi-Fiに接続してWebサーバを起動
```
プログラムを日本語に直すと以下のようになります。
```サーボを制御する宣言
wifi.pyからrun関数をインポート

Wi-FiのSSID
Wi-Fiのパスワード

HTMLの内容

Wi-Fiに接続してWebサーバを起動
```
#### 動作
プログラムを実行して、表示された「**IPアドレス**」にアクセスします。

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/IP_address.png" width="40%" />

IPアドレスはWebサイトの住所のことです。

Webサイトができて、「Hello World」が表示されたことが確認できます。  
ラズパイが「**Webサーバー**」になっているのです。

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/Web_HelloWorld.png" width="40%" />

### 💡Webサイト：応用問題

**🚀 きみだけのWebサイトをつくろう！カスタマイズ大作戦！**

これは、Webサイトをつくるための「HTML」を、パワーアップさせるガイドです！

#### **🏃‍♂️‍➡️スタート地点**

```html
html = """
<!doctype html>
<h1>Hello World</h1>
"""
```
#### **⭐ Webサイトをかっこよくする 4ステップ**
**元のプログラムに、これらのコードを追加するとどうなるか見てみよう！**

|  | 追加するコード | どこに入れる？ | 結果 |
| ----- | ----- | ----- | ----- |
| **1\. 土台づくり** | `<body> <h1>Hello World</h1></body>` | `<h1> </h1>` のそとがわ | Webページとして**正しくうごく**ための枠組みができます |
| **2\. 背景色** | `<body style="background-color: skyblue;">` | `<body>`の中 | **画面ぜんぶが水色** になります |
| **3\. 文字色** | `<h1 style="color: red;">` | `<h1>` の中 | 文字の色が**赤色**になります |
| **4\. 文をふやす** | `<p>これは追加された文です</p>` | `</h1>` のすぐ下 | 見出しの下に新しい文が追加されます |

 #### ✅完成コードの例

```html
html = """
<!doctype html>
<body style="background-color: skyblue;">
    <h1 style="color: red;">Hello World</h1>
    <p>これは追加された文です</p>
</body>
"""
```

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/Web_HelloWorld_2.png" width="40%" />

色を変えたり文字を追加したりして、自分だけのWebサイトを作ってみましょう。

## 作品制作：どこでもポチっとIoTスイッチ
学んだ内容を組み合わせて作品を制作しましょう。

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/learned.png" width="80%" />

今回はWi-Fiをつなげてパソコンから操作する作品にします。
無線通信でサーボモーターを動かす装置です。

### サーボモーターの接続
今までと同じ場所にサーボモーターをつなぎます。

### どこでもポチっとIoTスイッチのプログラム
```python
#Webボタンでサーボを動かす
from wifi import run_button                      # wifi.pyからrun_button関数をインポート
from picozero import Servo                       # サーボを使うためのライブラリ
from time import sleep                           # 待ち時間を入れるための関数

SSID = ''                                	     # Wi-FiのSSID
PASSWORD = ''                            	     # Wi-Fiのパスワード
servo = Servo(0, None, 0.0005, 0.0024)           # GP0にサーボを接続
servo.value = 45 / 180                           # はじめの角度（待機位置）

html = """
<!doctype html>
<button onclick=“fetch(‘/push’)”>サーボモーターを動かす</button>
"""                                              # Webページの内容
def push_servo():                                # ボタンが押されたときに呼ばれる処理
    servo.value = 45 / 180                       # 45°へ動かす
    sleep(0.15)                                  # 0.15秒待つ
    servo.value = 135 / 180                      # 135°へ動かす
    sleep(0.25)                                  # 0.25秒待つ
    servo.value = 45 / 180                       # 45°へ戻す

run_button(SSID, PASSWORD, html, push_servo)     # Wi-Fi接続してボタンWebサーバを起動
```

#### 動作
Webページのボタンを押すとサーボモータが動きます。
<video src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/videos/Web_servo.mp4?raw=true" width="60%" autoplay loop muted playsinline></video>

応用するとこんなこともできます・・・  
**どこでもポチっとできるガジェット**です！

 - 照明のスイッチを無線で操作
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/servo_light.png" width="30%" />

 - 猫じゃらしを無線で操作
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/servo_cat.png" width="30%" />

## おまけ：温度センサで温度を測る
#### 温度センサとは
 - 温度によって流れる電圧の大きさが変わります
 - 足が3本です  
 平らな面から見たときに
   - 左の足が＋（プラス）の電源
   - 真ん中の足が出力
   - 右の足が－（マイナス）
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/MCP9701.png" width="40%" />

[MCP9701データシート](https://akizukidenshi.com/goodsaffix/MCP9701-ETO.pdf) より引用

### 温度センサの接続
 - ラズパイの右上から5番目のピンの横に左の足を差し込みます
 - ラズパイの右上から7番目のピンの横に真ん中の足を差し込みます
 - ラズパイの右上から8番目のピンの横に右の足を差し込みます
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/tempsensor_connect.png" width="80%" />

### 温度センサのプログラム
```python
from picozero import TemperatureSensor  # ADCを電圧[V]に変換
from time import sleep		        # 待ち時間

ts = TemperatureSensor(28)              # GP28（ADC2）に温度センサを接続

while True: 				        # ずっと繰り返す
    v = ts.voltage                      # 電圧を取得
    temp = (v - 0.400) / 0.0195         # 電圧を温度に変換する式
    print(f"{temp:.3f}°C")		    # 温度を表示
    sleep(0.2)                          # 0.2秒待つ
```
プログラムを日本語に直すと以下のようになります。
```
温度センサを制御する宣言
待ち時間を指定する宣言

GPIO28番ピン(ADC2)を使用することをラズパイに伝える

ここから下が無限ループ
    温度センサから電圧を取得する
    電圧を温度に変換する
    温度を表示する
    0.2秒待つ
```
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/tempsensor_flow.png" width="100%" />

#### 動作
0.2秒ごとに温度を表示します。

<video src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/videos/temp1.mp4?raw=true" width="60%" autoplay loop muted playsinline></video>

シェルを右クリックして、「プロッターを表示」を押すと、グラフを見ることができます。

<video src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/videos/temp2.mp4?raw=true" width="70%" autoplay loop muted playsinline></video>

## おまけ：照度センサで明るさを測る
#### 照度センサとは
 - 明るさによって流れる電圧の大きさが変わります
 - 足が2本です  
### 照度センサの接続
 - ラズパイの左下から1番目のピンの横に片方の足を差し込みます
 - ラズパイの左上から3番目のピンの横にもう片方の足を差し込みます

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/illuminance_connect.png" width="80%" />

### 照度センサのプログラム
```python
from picozero import Button         # 照度センサ→Button扱い
from time import sleep              # 待ち時間

# GP15に照度センサの片足を接続（もう片足はGND）
light = Button(15, pull_up=True)

While True:                         # ずっと繰り返す
    if light.is_pressed: print("明るい") # もし 明るかったら「明るい」と表示
    else: print(“暗い”)        　# そうでなければ（暗かったら）「暗い」と表示
    sleep(0.1)                      # 0.1秒待つ
```
#### 動作
0.1秒ごとに明るいか暗いかを表示します。
___

制作：2026 仙台高専プログラミング部
