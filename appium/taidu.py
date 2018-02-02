import os
import unittest
from appium import webdriver
from time import sleep


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

print('start')
desired_caps = {} # 定义一个字典
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'LE67A06310143950'
desired_caps['appPackage'] = 'com.tude.android'
desired_caps['appActivity'] = '.base.SplashActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)

print("testcase")
# driver.find_element_by_id("com.tude.android:id/btn_profile").click();
driver.find_element_by_android_uiautomator("text(\"我的\")").click()
print("账号密码登录：",driver.page_source.find("账号密码登录"))
driver.find_element_by_accessibility_id()
driver.find_element_by_id("com.tude.android:id/tv_account").click()
driver.find_element_by_id("com.tude.android:id/et_account").send_keys('18521035133')
driver.find_element_by_id("com.tude.android:id/et_password").send_keys('111111')
driver.quit()
sleep(2)

## 查找元素