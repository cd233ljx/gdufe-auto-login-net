import json
import requests
import socket
import time
import os
import sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def get_exe_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def load_config():
    config_path = os.path.join(get_exe_dir(), 'config.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return '172.31.28.69'


def show_notification(title, message):
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        icon_path = resource_path('Ostar37.ico')
        toaster.show_toast(title, message, icon_path=icon_path, duration=5)
    except Exception as e:
        try:
            from plyer import notification
            notification.notify(
                title=title,
                message=message,
                app_name='校园网自动登录',
                timeout=5
            )
        except:
            pass


def login():
    config = load_config()
    student_id = config['student_id']
    password = config['password']
    local_ip = get_local_ip()
    
    url = 'http://100.64.13.17:801/eportal/portal/login'
    
    params = {
        'callback': 'dr1003',
        'login_method': '1',
        'user_account': f',0,{student_id}',
        'user_password': password,
        'wlan_user_ip': local_ip,
        'wlan_user_ipv6': '',
        'wlan_user_mac': '000000000000',
        'wlan_ac_ip': '100.64.13.18',
        'wlan_ac_name': '',
        'jsVersion': '4.1.3',
        'terminal_type': '1',
        'lang': 'zh-cn',
        'v': '5464'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        if '认证成功' in response.text or 'result":1' in response.text or 'result":0' in response.text:
            show_notification('校园网登录', '登录成功！')
            print('登录成功！')
        else:
            show_notification('校园网登录', '登录失败，请检查账号密码')
            print(f'登录失败：{response.text}')
            
    except Exception as e:
        show_notification('校园网登录', '登录异常，请检查网络')
        print(f'登录异常：{str(e)}')


if __name__ == '__main__':
    login()
