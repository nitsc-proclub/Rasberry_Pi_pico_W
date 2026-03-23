from machine import Pin, SPI
import machine
import framebuf
import utime
import random
import rp2
from misakifont import MisakiFont


EPD_WIDTH = 122
EPD_HEIGHT = 250

RST_PIN = 12
DC_PIN = 8
CS_PIN = 9
BUSY_PIN = 13

MIN_REFRESH_INTERVAL_SEC = 180
LONG_PRESS_MS = 3000

led = machine.Pin("LED", machine.Pin.OUT)


class EPD_2in13_B_V4_Landscape:
    def __init__(self):
        self.reset_pin = Pin(RST_PIN, Pin.OUT)
        self.busy_pin = Pin(BUSY_PIN, Pin.IN, Pin.PULL_UP)
        self.cs_pin = Pin(CS_PIN, Pin.OUT)

        # ここ重要: FrameBuffer用に幅を8の倍数へ切り上げる
        if EPD_WIDTH % 8 == 0:
            self.width = EPD_WIDTH
        else:
            self.width = (EPD_WIDTH // 8) * 8 + 8

        self.height = EPD_HEIGHT

        self.spi = SPI(1)
        self.spi.init(baudrate=4_000_000)
        self.dc_pin = Pin(DC_PIN, Pin.OUT)

        self.buffer_black = bytearray(self.height * self.width // 8)
        self.buffer_red = bytearray(self.height * self.width // 8)

        self.imageblack = framebuf.FrameBuffer(
            self.buffer_black, self.height, self.width, framebuf.MONO_VLSB
        )
        self.imagered = framebuf.FrameBuffer(
            self.buffer_red, self.height, self.width, framebuf.MONO_VLSB
        )

        self.init()

    def digital_write(self, pin, value):
        pin.value(value)

    def digital_read(self, pin):
        return pin.value()

    def delay_ms(self, delaytime):
        utime.sleep(delaytime / 1000.0)

    def spi_writebyte(self, data):
        self.spi.write(bytearray(data))

    def module_exit(self):
        self.digital_write(self.reset_pin, 0)

    def reset(self):
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(50)
        self.digital_write(self.reset_pin, 0)
        self.delay_ms(2)
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(50)

    def send_command(self, command):
        self.digital_write(self.dc_pin, 0)
        self.digital_write(self.cs_pin, 0)
        self.spi_writebyte([command])
        self.digital_write(self.cs_pin, 1)

    def send_data(self, data):
        self.digital_write(self.dc_pin, 1)
        self.digital_write(self.cs_pin, 0)
        self.spi_writebyte([data])
        self.digital_write(self.cs_pin, 1)

    def send_data1(self, buf):
        self.digital_write(self.dc_pin, 1)
        self.digital_write(self.cs_pin, 0)
        self.spi.write(bytearray(buf))
        self.digital_write(self.cs_pin, 1)

    def ReadBusy(self):
        print("busy")
        while self.digital_read(self.busy_pin) == 1:
            self.delay_ms(10)
        print("busy release")
        self.delay_ms(20)

    def TurnOnDisplay(self):
        self.send_command(0x20)
        self.ReadBusy()

    def SetWindows(self, Xstart, Ystart, Xend, Yend):
        self.send_command(0x44)
        self.send_data((Xstart >> 3) & 0xFF)
        self.send_data((Xend >> 3) & 0xFF)

        self.send_command(0x45)
        self.send_data(Ystart & 0xFF)
        self.send_data((Ystart >> 8) & 0xFF)
        self.send_data(Yend & 0xFF)
        self.send_data((Yend >> 8) & 0xFF)

    def SetCursor(self, Xstart, Ystart):
        self.send_command(0x4E)
        self.send_data(Xstart & 0xFF)

        self.send_command(0x4F)
        self.send_data(Ystart & 0xFF)
        self.send_data((Ystart >> 8) & 0xFF)

    def init(self):
        print("init")
        self.reset()

        self.ReadBusy()
        self.send_command(0x12)  # SWRESET
        self.ReadBusy()

        self.send_command(0x01)
        self.send_data(0xF9)
        self.send_data(0x00)
        self.send_data(0x00)

        self.send_command(0x11)
        self.send_data(0x07)

        self.SetWindows(0, 0, self.width - 1, self.height - 1)
        self.SetCursor(0, 0)

        self.send_command(0x3C)
        self.send_data(0x05)

        self.send_command(0x18)
        self.send_data(0x80)

        self.send_command(0x21)
        self.send_data(0x80)
        self.send_data(0x80)

        self.ReadBusy()

    def display(self):
        # ここは前に動いていた版のまま
        self.send_command(0x24)
        for j in range(int(self.width / 8) - 1, -1, -1):
            for i in range(0, self.height):
                self.send_data(self.buffer_black[i + j * self.height])

        self.send_command(0x26)
        for j in range(int(self.width / 8) - 1, -1, -1):
            for i in range(0, self.height):
                self.send_data(self.buffer_red[i + j * self.height])

        self.TurnOnDisplay()

    def Clear(self, colorblack, colorred):
        self.send_command(0x24)
        self.send_data1([colorblack] * self.height * int(self.width / 8))

        self.send_command(0x26)
        self.send_data1([colorred] * self.height * int(self.width / 8))

        self.TurnOnDisplay()

    def sleep(self):
        self.send_command(0x10)
        self.send_data(0x01)
        self.delay_ms(2000)
        self.module_exit()


def jpredchar(fd, epd, x, y):
    for row in range(0, 7):
        for col in range(0, 7):
            if (0x80 >> col) & fd[row]:
                epd.imagered.pixel(col + x, row + y, 0x00)


def jpblackchar(fd, epd, x, y):
    for row in range(0, 7):
        for col in range(0, 7):
            if (0x80 >> col) & fd[row]:
                epd.imageblack.pixel(col + x, row + y, 0x00)


def jpredtext(text, x, y, mf, epd):
    for c in text:
        d = mf.font(ord(c))
        jpredchar(d, epd, x, y)
        x += 9


def jpblacktext(text, x, y, mf, epd):
    for c in text:
        d = mf.font(ord(c))
        jpblackchar(d, epd, x, y)
        x += 9


def clear_canvas(epd):
    epd.imageblack.fill(0xFF)
    epd.imagered.fill(0xFF)


def draw_center_text_black(epd, mf, text, y):
    width = len(text) * 9
    x = max(0, (250 - width) // 2)
    jpblacktext(text, x, y, mf, epd)


def draw_center_text_red(epd, mf, text, y):
    width = len(text) * 9
    x = max(0, (250 - width) // 2)
    jpredtext(text, x, y, mf, epd)


def show_wait_screen(epd, mf):
    clear_canvas(epd)
    draw_center_text_black(epd, mf, "おみくじ", 15)
    draw_center_text_black(epd, mf, "BOOTSELを", 35)
    draw_center_text_black(epd, mf, "おしてね", 50)
    draw_center_text_red(epd, mf, "[ ひけます ]", 75)
    epd.display()
    print("待機画面を表示しました")


def show_omikuji(epd, mf, fortune):
    clear_canvas(epd)
    draw_center_text_black(epd, mf, "きょうの うんせい", 8)
    draw_center_text_red(epd, mf, fortune["result"], 35)

    y = 65
    for line in fortune["text"]:
        draw_center_text_black(epd, mf, line, y)
        y += 15

    epd.display()
    print("表示中:", fortune["result"])


def bootsel_pressed():
    try:
        return rp2.bootsel_button() == 1
    except Exception as e:
        print("BOOTSEL read error:", e)
        return False


def update_led(ready, pressed, press_start_ms):
    # READY: 点灯
    if ready:
        led.on()
        return

    # COOLDOWN: 点滅
    # 長押し中は何もしない
    if pressed and press_start_ms is not None:
        hold_ms = utime.ticks_diff(utime.ticks_ms(), press_start_ms)
        if hold_ms >= LONG_PRESS_MS:
            return

    led.value((utime.ticks_ms() // 500) % 2)


if __name__ == "__main__":
    epd = EPD_2in13_B_V4_Landscape()
    mf = MisakiFont()

    omikuji_data = [
        {
            "result": "だいきち",
            "text": ["さいこうの ひ", "えがおで いこう", "いいこと ありそう"]
        },
        {
            "result": "ちゅうきち",
            "text": ["なかなか いいひ", "あせらず いこう", "まえに すすもう"]
        },
        {
            "result": "しょうきち",
            "text": ["ちいさな しあわせ", "みつかるかも", "ゆっくり いこう"]
        },
        {
            "result": "きち",
            "text": ["おだやかな ひ", "ていねいに いこう", "かんしゃが だいじ"]
        },
        {
            "result": "きょう",
            "text": ["きをつけてね", "しんちょうに", "あしたに きたい"]
        }
    ]

    last_update_sec = None
    press_start_ms = None

    try:
        show_wait_screen(epd, mf)

        while True:
            now_sec = utime.time()
            pressed = bootsel_pressed()

            if last_update_sec is None:
                ready = True
            else:
                ready = (now_sec - last_update_sec) >= MIN_REFRESH_INTERVAL_SEC

            update_led(ready, pressed, press_start_ms)

            if pressed:
                if press_start_ms is None:
                    press_start_ms = utime.ticks_ms()

                hold_ms = utime.ticks_diff(utime.ticks_ms(), press_start_ms)

                if hold_ms >= LONG_PRESS_MS:
                    print("終了処理を実行します...")
                    epd.Clear(0xFF, 0xFF)
                    epd.sleep()
                    led.off()

                    while bootsel_pressed():
                        utime.sleep_ms(50)
                    print("完了しました。")
                    break

            else:
                if press_start_ms is not None:
                    hold_ms = utime.ticks_diff(utime.ticks_ms(), press_start_ms)

                    # 短押し
                    if hold_ms < LONG_PRESS_MS:
                        if ready:
                            fortune = random.choice(omikuji_data)
                            show_omikuji(epd, mf, fortune)
                            last_update_sec = utime.time()
                        else:
                            print("まだ待機中なので画面更新しません")

                    press_start_ms = None

            utime.sleep_ms(50)

    except KeyboardInterrupt:
        print("終了処理を実行します...")
        epd.Clear(0xFF, 0xFF)
        epd.sleep()
        led.off()
        print("完了しました。")
        