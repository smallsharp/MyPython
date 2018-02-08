'''
Created on 2017年9月26日
# 这个例子os.system接收命令行参数，运行参数指令，我们在cmd命令行运行sys.argv.py脚本，具体命令：>>>> python using sys.argv.py "whoami"，将获取当前运行脚本的用户信息。
@author: cm
'''

# 
import sys,os   
print(sys.argv)                #打印输出命令行执行参数列表。
os.system(sys.argv[1])         #打印输出“系统命令执行结果”