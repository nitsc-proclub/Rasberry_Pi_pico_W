# 温度センサ（MCP9701を想定）
from picozero import TemperatureSensor  # ADCを電圧[V]に変換
from time import sleep					# 待ち時間

ts = TemperatureSensor(28)              # GP28（ADC2）に温度センサを接続

while True: 							# ずっと繰り返す
    v = ts.voltage                      # 電圧を取得
    temp = (v - 0.400) / 0.0195         # 電圧を温度に変換する式：0°C=0.400V, 19.5mV/°C
    print(f"{temp:.3f}°C")				# 温度を表示
    sleep(0.1)                          # 0.1秒待つ