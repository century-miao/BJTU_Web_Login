import requests
from plyer import notification  # 用于弹出通知
import subprocess  # 用于执行命令行命令
from pywifi import PyWiFi, const, Profile
import time

userid = 'username'
password = 'password'
target_ssid = 'web.wlan.bjtu'


def check_network():
    # 这里可以使用一个更复杂的方法来确切地判断是否连接到了特定的网络
    # 例如通过检查WLAN的SSID
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
    return 'web.wlan.thu' in result.stdout


def is_connected_to_target_network(target_ssid):
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]

    ifaces.scan()  # 扫描周围的WiFi
    time.sleep(2)  # 稍等两秒，等待扫描结果
    results = ifaces.scan_results()


    for network in results:
        if network.ssid == target_ssid:
            return True
    return False


def login():
    url = 'http://10.10.43.3'

    # 用户名与密码

    login_payload = {
        'DDDDD': userid,
        'upass': password,
        'R1': '0',
        'R3': '0',  # 如果COM port是一个具体的值，替换成那个值
        'R6': '0'
    }

    try:
        response = requests.post(url, data=login_payload)
        if response.status_code == 200:
            # 这里可以添加更多的检查来确认登录是否成功
            print("登录成功")
            return True
        else:
            print("登录失败，响应码：", response.status_code)
    except requests.exceptions.RequestException:
        return False


def notify_user():
    notification.notify(
        title='网络登录通知',
        message='您已成功登录到网络！',
        app_icon=None,  # 可以指定一个.ico图标路径
        timeout=10,  # 通知显示的时间
    )


def notify_user_fail():
    notification.notify(
        title='网络登录通知',
        message='未能连接到校园网！',
        app_icon=None,  # 可以指定一个.ico图标路径
        timeout=10,  # 通知显示的时间
    )

def notify_password():
    notification.notify(
        title='网络登录通知',
        message='用户名密码错误',
        app_icon=None,  # 可以指定一个.ico图标路径
        timeout=10,  # 通知显示的时间
    )


if __name__ == '__main__':

    if is_connected_to_target_network(target_ssid):
        if login():
            notify_user()
        else:
            notify_password()
    else:
        notify_user_fail()
