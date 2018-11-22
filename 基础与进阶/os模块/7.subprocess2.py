#coding=utf-8

import subprocess

# start server
appium_path = r"D:\nodejs\new_modules\appium.cmd"
# server_cmd = appium_path + ' -p 26270 -bp 27235 -U 85GBBMA2353T --local-timezone  --command-timeout 1200 --log-timestamp  --session-override '
# server = subprocess.run(appium_path, stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=False)  # check=False时运行错误不检查
server = subprocess.Popen(appium_path, stderr=subprocess.PIPE, stdout=subprocess.PIPE)  # check=False时运行错误不检查
# server.wait()

if server.returncode != 0:
    print("Error")

print("ok"*20)