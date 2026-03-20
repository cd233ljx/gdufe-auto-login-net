# 广财校园网自动登录

基于 Python 实现的校园网自动登录工具。

## 功能特点

- ✅ 自动获取本机 IP
- ✅ 一键登录校园网
- ✅ Windows 右下角通知提示
- ✅ 支持自定义图标
- ✅ 配置文件独立存储


## 项目结构

```
auto-login-net/
├── login.py          # 主程序
├── config.json       # 配置文件（需自行创建）
├── requirements.txt  # 依赖包列表
├── build.py          # 打包脚本
├── Ostar37.ico       # 程序图标
├── venv/             # 虚拟环境
└── dist/             # 打包输出目录
```

## 配置说明

复制 `config.json.example` 为 `config.json`，然后填写你的学号和密码：

```json
{
  "student_id": "你的学号",
  "password": "你的密码"
}
```

## 开发环境

### 1. 安装依赖

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. 运行程序

```powershell
.\venv\Scripts\python.exe login.py
```

## 发行版使用说明

打包完成后，将以下文件放在同一目录：
- `校园网自动登录.exe`
- `config.json`

双击运行即可！

## 依赖库

- `requests` - HTTP 请求
- `plyer` - 跨平台通知
- `win10toast` - Windows 通知
- `pyinstaller` - 打包工具
- `pillow` - 图像处理（用于图标转换）
- `setuptools` - Python 工具

