#st7789が搭載されているディスプレイとオルタネイトのボタンが必要
import gc
import time
import st7789
from machine import Pin,SPI
from misakifont import MisakiFont
import urequests
import ujson
import network
import tft_config
import random

gc.collect()

tft = tft_config.config(0)
switch = Pin(0, Pin.IN, Pin.PULL_UP)
tft.init()

mf = MisakiFont()

def connectnetwork(ssid,password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('接続待ち...')
        time.sleep(1)
    if wlan.status() != 3:
        raise RuntimeError('ネットワーク接続失敗')
    else:
        print('接続完了')
        status = wlan.ifconfig()
        print( 'IPアドレス = ' + status[0] )
        
def text(string,x,y,fcolor,fsize,sleep):
    for c in string:
        d = mf.font(ord(c))
        show_bitmap(d, x, y, fcolor, fsize)
        x += 8 * fsize
        if x >= 240:
            x = 0
            y += 8 * fsize
        if y >= 320:
            y = 0
        time.sleep(sleep)

def show_bitmap(fd, x, y, color, size):
    for row in range(0, 7):
        for col in range(0, 7):
            if (0x80 >> col) & fd[row]:
                tft.fill_rect(int(x + col * size), int(y + row * size), size, size, color)

def gemini(prompt):
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=AIzaSyBieTOu8DVz9ub-DxjoOi464ECCld86GWo'
    header = {'Content-Type': 'application/json'}
    contents = {"contents": [{"parts":[{"text": prompt}]}]}
    response = urequests.post(url,data = ujson.dumps(contents).encode("utf-8"),headers=header)
    r = response.json()['candidates'][0]['content']['parts'][0]['text']
    return r

def randomluck():
    luck = ["大きち","きち","中きち","小きち","末きち"]
    res = random.choice(luck)
    if res == "大きち":
        ans = gemini("大吉のおみくじに書いてあるアドバイスを考え、考えた文章だけを出力してください。また、漢字を使わずに100文字以内にし簡潔にしてください。")
        text(res,0,100,st7789.RED,10,0)
        text(ans,0,200,st7789.WHITE,2,0)
    elif res == "きち":
        ans = gemini("吉のおみくじに書いてあるアドバイスを考え、考えた文章だけを出力してください。また、漢字を使わずに100文字以内にし簡潔にしてください。")
        text(res,40,100,st7789.YELLOW,10,0)
        text(ans,0,200,st7789.WHITE,2,0)
    elif res == "中きち":
        ans = gemini("中吉のおみくじに書いてあるアドバイスを考え、考えた文章だけを出力してください。また、漢字を使わずに100文字以内にし簡潔にしてください。")
        text(res,0,100,st7789.GREEN,10,0)
        text(ans,0,200,st7789.WHITE,2,0)
    elif res == "小きち":
        ans = gemini("小吉のおみくじに書いてあるアドバイスを考え、考えた文章だけを出力してください。また、漢字を使わずに100文字以内にし簡潔にしてください。")
        text(res,0,100,st7789.CYAN,10,0)
        text(ans,0,200,st7789.WHITE,2,0)
    else:
        ans = gemini("末吉のおみくじに書いてあるアドバイスを考え、考えた文章だけを出力してください。また、漢字を使わずに100文字以内にし簡潔にしてください。")
        text(res,0,100,st7789.BLUE,10,0)
        text(ans,0,200,st7789.WHITE,2,0)
    

def main():
    tft.init()
    text("おみくじの",40,25,st7789.WHITE,4,0.02)
    time.sleep(2)
    text("結果は...",24,57,st7789.WHITE,4,0.25)
    randomluck()

connectnetwork("銀狼","furiyamanuame")

alrpre = 0
while True:
    if switch.value() == 0:
        if alrpre == 0:
            main() 
            alrpre = 1
    else:
        if alrpre == 1:
            alrpre = 0
    time.sleep(0.01)




