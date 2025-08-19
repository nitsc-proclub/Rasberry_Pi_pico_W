# Rasberry Pi pico W

## 目的
Rasberry Pi pico W の使い方、ソースコードを共有するためのリポジトリです。  
「とうほくプロコン」のワークショップ手伝いで作成したサンプルの解説も行います。

## 方針
 - **小中学生も見る**ことを想定し、なるべく簡潔に書く
 - コメントを多めに入れる
 - ライブラリとして、[**picozero**](https://github.com/RaspberryPiFoundation/picozero) を使用することを推奨

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
💡`print`に計算の式を入れて遊んでみましょう

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
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/breadboard.png" width="80%" />
- ボードの内部で線がつながっています
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/breadboard_line.png" width="80%" />

#### ラズパイをボードに差し込む
画像のように差し込みましょう
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/main/images/breadboard_rasberrypi.png" width="80%" />

## LEDを光らせる
#### LEDとは
 - 発光ダイオード
 - 電気を流すと光ります
 - 足が2本です
   - 足が長い方が＋（プラス）
   - 足が短い方－（マイナス）
   
購入はこちら：https://akizukidenshi.com/catalog/g/g111577/

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

___
制作：2025 仙台高専プログラミング部
