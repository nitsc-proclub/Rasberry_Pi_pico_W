# Rasberry Pi pico W

## 目的
Rasberry Pi pico W の使い方、ソースコードを共有するためのリポジトリです。  
「とうほくプロコン」のワークショップ手伝いで作成したサンプルの解説も行います。

## 方針
 - **小中学生も見る**ことを想定し、なるべく簡潔に書く
 - コメントを多めに入れる
 - ライブラリとして、[**picozero**](https://github.com/RaspberryPiFoundation/picozero) を使用することを推奨

## 共有サンプル
 - [単一ファイルで動くサンプル](https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/tree/5818355007a6347ab4c75040784721f0ee3f67ed/single-file-examples)

___
#### 以下はMarkDownで書いたWEB資料です。HTMLに変換したものを、GitHub Pagesで公開しています。
https://nitsc-proclub.github.io/Rasberry_Pi_pico_W/

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/page.png" width="80%" />

# とうほくプロコンワークショップ「ラズパイPicoで酷暑を乗り切ろう」

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

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/videos/LED.gif" width="30%" />

___
> [!IMPORTANT]
> **これ以降の内容は未完成です🙇今後更新していきます。**
___

## 温度センサで温度を測る
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
from time import sleep			        # 待ち時間

ts = TemperatureSensor(28)              # GP28（ADC2）に温度センサを接続

while True: 					        # ずっと繰り返す
    v = ts.voltage                      # 電圧を取得
    temp = (v - 0.400) / 0.0195         # 電圧を温度に変換する式
    print(f"{temp:.3f}°C")			    # 温度を表示
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

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/videos/temp1.mp4" width="30%" />

シェルを右クリックして、「プロッターを表示」を押すと、グラフを見ることができます。

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/videos/temp2.mp4" width="30%" />


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

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/videos/servo.mp4" width="30%" />

## 作品制作：暑いときに自動であおぐうちわ
学んだ内容を組み合わせて作品を制作しましょう。

<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/learned.png" width="80%" />

今回は例として、「暑いときに自動であおぐうちわ」を作ってみます。  
もし温度が **しきい値** （基準の値） よりも高ければモーターが動くようにします。  
このような処理を **条件分岐** と言います。
                
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/fan_flow.png" width="65%" />

### サーボモーターと温度センサの接続
今までと同じ場所にサーボモーターと温度センサをつなぎます。

### 暑いときに自動であおぐうちわのプログラム
```python
from picozero import TemperatureSensor, Servo    # 温度センサとサーボを使用
from time import sleep                           # 待ち時間

TH = 28.0                                        # しきい値(温度)：これを超えたら作動

servo = Servo(0, None, 0.0005, 0.0024)	       # サーボ(GP0)
ts = TemperatureSensor(28)                       # 温度センサ(GP28/ADC2)

while True:                                      # 無限ループ
    temp = (ts.voltage - 0.400) / 0.0195         # 電圧→温度[℃]に変換（MCP9701）
    print(f"{temp:.1f}℃")                       # 温度を表示
    if temp > TH:                                # しきい値を超えた？
        servo.value = 45/180                     # 45度に動かす
        sleep(0.5)                               # 0.5秒待つ
        servo.value = 135/180                    # 135度に動かす
        sleep(0.5)                               # 0.5秒待つ
```
ここで、しきい値の値は`28.0`だけでなく、自由に数字を入力して大丈夫です。
```python
TH = 28.0                                        # しきい値(温度)：これを超えたら作動
```
「温度センサを手で温めたら何度になるか...？」などを記録して、「しきい値」を決めましょう。
                
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/temperature_measurement.png" width="70%" />

## 照度センサで明るさを測る
### 照度センサの接続
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
___

制作：2025 仙台高専プログラミング部
