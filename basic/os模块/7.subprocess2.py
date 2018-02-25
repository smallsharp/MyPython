#coding=utf-8

import subprocess

# start server
appium_path = r"D:\nodejs\new_modules\appium.cmd"
server_cmd = appium_path + ' -p 26270 -bp 27235 -U 85GBBMA2353T --local-timezone  --command-timeout 1200 --log-timestamp  --session-override '
# server = subprocess.Popen(server_cmd)
import os
server = os.system(server_cmd)

# print(server.pid)
print("ok"*20)

# print(server.wait())
# server.kill()