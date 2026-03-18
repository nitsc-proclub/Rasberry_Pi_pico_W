import network
import socket
import time


# 接続失敗として扱うWi-Fi状態
_WIFI_ERROR_STATES = ("WRONG_PASSWORD", "NO_AP_FOUND", "CONNECT_FAIL")


def _status_text(wlan):
    """WLAN.status() の値を読みやすい文字列に変換する。"""
    status = wlan.status()
    labels = {
        getattr(network, "STAT_IDLE", 0): "IDLE",
        getattr(network, "STAT_CONNECTING", 1): "CONNECTING",
        getattr(network, "STAT_WRONG_PASSWORD", -3): "WRONG_PASSWORD",
        getattr(network, "STAT_NO_AP_FOUND", -2): "NO_AP_FOUND",
        getattr(network, "STAT_CONNECT_FAIL", -1): "CONNECT_FAIL",
        getattr(network, "STAT_GOT_IP", 3): "GOT_IP",
    }
    return labels.get(status, str(status))


def connect_wifi(ssid, password, retry_sec=0.5, timeout_sec=20, country="JP"):
    """Wi-Fiに接続し、接続済みのWLANオブジェクトを返す。"""
    if not ssid:
        raise ValueError("SSID is empty. Set SSID in 無線接続.py")

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # ファームウェアによっては接続前に国コード設定が必要。
    if hasattr(network, "country") and country:
        try:
            network.country(country)
        except Exception:
            pass

    if not wlan.isconnected():
        wlan.connect(ssid, password)
        start = time.time()
        while not wlan.isconnected():
            elapsed = time.time() - start
            status_name = _status_text(wlan)

            if status_name in _WIFI_ERROR_STATES:
                raise RuntimeError("Wi-Fi failed: %s" % status_name)

            if elapsed >= timeout_sec:
                raise TimeoutError(
                    "Wi-Fi timeout after %ss (status=%s)" % (timeout_sec, status_name)
                )

            time.sleep(retry_sec)

    return wlan


def _sendall(client, data):
    """sendall未対応環境でも送信できるようにする。"""
    try:
        client.sendall(data)
    except AttributeError:
        client.send(data)


def _http_ok(content_type, body):
    """HTTP 200レスポンスを生成する。"""
    if isinstance(body, str):
        body = body.encode("utf-8")

    header = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: %s\r\n"
        "Connection: close\r\n"
        "Cache-Control: no-store\r\n"
        "\r\n" % content_type
    )
    return header.encode("utf-8") + body


def _bind_server(addr, backlog=5, retry_sec=0.2, timeout_sec=5):
    """サーバソケットを生成し、ポート競合時は短時間だけ再試行する。"""
    server = socket.socket()

    if hasattr(socket, "SO_REUSEADDR"):
        try:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception:
            pass

    start = time.time()
    while True:
        try:
            server.bind(addr)
            server.listen(backlog)
            return server
        except OSError as e:
            # Errno 98: address already in use
            if len(e.args) > 0 and e.args[0] == 98 and (time.time() - start) < timeout_sec:
                time.sleep(retry_sec)
                continue
            try:
                server.close()
            except Exception:
                pass
            raise


def run(
    ssid,
    password,
    html,
    host="0.0.0.0",
    port=80,
    wifi_timeout_sec=20,
    bind_timeout_sec=5,
):
    """Wi-Fi接続後にHTMLを返すシンプルなWebサーバを起動する。"""
    wlan = connect_wifi(ssid, password, timeout_sec=wifi_timeout_sec)

    addr = socket.getaddrinfo(host, port)[0][-1]
    server = _bind_server(addr, timeout_sec=bind_timeout_sec)

    # アクセスすべきURLだけ表示する。
    ip = wlan.ifconfig()[0]
    if port == 80:
        print("アクセス先: http://%s/" % ip)
    else:
        print("アクセス先: http://%s:%s/" % (ip, port))

    try:
        while True:
            client, _ = server.accept()
            try:
                # リクエスト内容は見ず、常に同じHTMLを返す。
                client.settimeout(1.0)
                _ = client.recv(1024)
                _sendall(client, _http_ok("text/html; charset=utf-8", html))
            except Exception:
                pass
            finally:
                client.close()
    except KeyboardInterrupt:
        pass
    finally:
        try:
            server.close()
        except Exception:
            pass
        try:
            wlan.disconnect()
        except Exception:
            pass
            