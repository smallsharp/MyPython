import os

res = os.popen("adb devices")
print(res.read())

# List of devices attached