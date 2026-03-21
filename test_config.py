import json
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


def check_needs_config(config):
    default_values = ['你的学号', '你的密码', '', None]
    return config.get('student_id') in default_values or config.get('password') in default_values


def save_config(config):
    config_path = os.path.join(get_exe_dir(), 'config.json')
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def setup_config():
    print('首次运行，请配置账号信息：')
    student_id = input('请输入学号：').strip()
    password = input('请输入密码：').strip()
    
    config = {
        'student_id': student_id,
        'password': password
    }
    save_config(config)
    print('配置已保存！')
    return config


def load_config():
    config_path = os.path.join(get_exe_dir(), 'config.json')
    
    if not os.path.exists(config_path):
        return setup_config()
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    if check_needs_config(config):
        return setup_config()
    
    return config


if __name__ == '__main__':
    print('测试配置功能...')
    config = load_config()
    print(f'加载到的配置：')
    print(f'学号: {config["student_id"]}')
    print(f'密码: {config["password"]}')
    print('配置功能测试完成！')
