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
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/95013959a7ad81ae68fc6c94ae27900b487d3585/images/cable_connect.png" width="80%" />
3. Thonyでラズパイを使用する設定を行う
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/95013959a7ad81ae68fc6c94ae27900b487d3585/images/thony_setting.png" width="80%" />

## プログラムを書こう 
### print文
Thonyでコードを打ち込んで「実行ボタン▶️」を押しましょう。
```python
print("Hello, World!")
```
実行結果
<img src="https://github.com/nitsc-proclub/Rasberry_Pi_pico_W/blob/95013959a7ad81ae68fc6c94ae27900b487d3585/images/result1.png" width="80%" />
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

<br>
<details open>
<summary>計算式の例</summary>

**例➀**
```python
print(6 / 3)
```
<details>
<summary>➀の実行結果</summary>

```python
2
```
6わる3は2です。
</details><br>

**例➁**
```python
print(2 * 4)
```
<details>
<summary>➁の実行結果</summary>

```python
8
```
2かける4は8です。
</details><br>

**例➂**
```python
print(5 + 4)
```
<details>
<summary>➂の実行結果</summary>

```python
9
```
5たす4は9です。
</details><br>
</details>
