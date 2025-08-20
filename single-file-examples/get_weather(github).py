import requests
import network
import ujson
import time
import machine

#LED設定
LED1 = machine.Pin(1, machine.Pin.OUT)
LED2 = machine.Pin(2, machine.Pin.OUT)
LED3 = machine.Pin(3, machine.Pin.OUT)
LED4 = machine.Pin(4, machine.Pin.OUT)

LED1.value(0)
LED2.value(0)
LED3.value(0)
LED4.value(0)

#ネット接続 接続するまで進まない
SSID = 'YOUR SSID'
PW = 'YOUR PASSWORD'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PW)
while wlan.isconnected() == False:
    print('Connecting to Wi-Fi router...')
    LED4.value(1)
    time.sleep(0.5)
    LED4.value(0)
    time.sleep(0.5)
print("Connected")

#気象庁からjsonを持ってくる関数
def get_weather():
    global LED1
    global LED2
    global LED3
    global LED4
    LED1.value(0)
    LED2.value(0)
    LED3.value(0)
    LED4.value(0)
    # 気象庁データの取得
    jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/040000.json"
    response = requests.get(jma_url)
    jma_json = ujson.loads(response.text)
    print("json get complete")

    # 気象jsonの今日の気象データを変数に格納
    jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][0]
    jma_weathercode = jma_json[0]["timeSeries"][0]["areas"][0]["weatherCodes"][0]
    
    # 全角スペースの削除
    jma_weather = jma_weather.replace('　', '')

    print(jma_weather)
    print(jma_weathercode)
    
    #weathercodeを数値に変換
    wc = int(jma_weathercode)
    
    #weathercode対応表に合わせてLEDを点灯
    if (wc < 182) and (wc > 99) :
        LED1.value(1)
    elif(wc < 282) and (wc > 199) :
        LED2.value(1)
    elif(wc < 382) and (wc > 299) :
        LED3.value(1)
    
    if(wc < 182) and (wc > 100) :
        LED4.value(1)
    elif(wc < 282) and (wc > 200) and wc != 209 :
        LED4.value(1)
    elif(wc < 382) and (wc > 300) :
        LED4.value(1)
    
    time.sleep(5)
    LED1.value(0)
    LED2.value(0)
    LED3.value(0)
    LED4.value(0)
#最初の処理
get_weather()

#bootselボタンが押されたら再度実行
while True:
    if rp2.bootsel_button() == 1:
        LED1.value(0)
        LED2.value(0)
        LED3.value(0)
        
        for i in range(4) :
            LED4.value(1)
            time.sleep(0.2)
            LED4.value(0)
            time.sleep(0.2)
        get_weather()
        time.sleep(1)