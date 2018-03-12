# coding=utf-8
"""
@Time:2018-03-1217:36
@Author:lfl5207
"""
import os
import re


def check_state():
    state = ["设备已连接", "没有检测到设备连接！", "设备已离线"]
    res = os.popen("adb get-state").read().strip()
    print(res)
    if res == "device":
        return state[0]
    elif res.find("error"):
        return state[1]
    else:
        return state[2]


def current_package():
    reg = re.compile(r'name=(.+?)/')
    res = current_application()

    try:
        return re.findall(reg, res)[0]
    except Exception:
        return ""


def current_activity():
    reg = re.compile(r'name=(.+?)\)')

    try:
        return re.findall(reg, current_application())[0]
    except Exception:
        return ""


def current_application():
    return os.popen("adb shell dumpsys window w | findstr \/ | findstr name=").read()


def serial_no():
    return os.popen("adb shell getprop ro.serialno").read().strip()


if __name__ == '__main__':
    # print(current_package())
    # print(current_activity())
    print(check_state())
