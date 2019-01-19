# coding=utf-8

import subprocess

command1 = "adb devices"

# 3.5后，推荐使用run
res = subprocess.run(command1, stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=False)  # check=False时运行错误不检查
# res = subprocess.run(command1, stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True) # check=False时运行错误不检查

# 执行的参数
print(res.args)

# 执行结果状态码
if res.returncode == 0:
    print('success')

# 执行正确的结果
print(res.stdout)

# 执行出错的结果
print(res.stderr)

# --------------------------------------------------------------------------------------------------------------------------

import subprocess

command2 = r"D:\Apps\nodejs\new_modules\appium.cmd"

# p1 = subprocess.run(command2, stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True)  # check=False时运行错误不检查
# print(p1.stdout)
# print(p1.returncode)
import requests,time


p2 = subprocess.Popen(command2, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# p2 = subprocess.Popen(command2, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# 如果之前已经启动了服务，第二次启动失败时，需要处理
for i in range(20):
    try:
        resp = requests.get('http://127.0.0.1:4723/wd/hub/status')
        print(resp.status_code)
        if resp.status_code==200:
            break
        time.sleep(2)
    except:
        print('error')

print('链接成功！')