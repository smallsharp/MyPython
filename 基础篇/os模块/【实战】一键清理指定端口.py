import subprocess
import re

cmd1 = 'netstat -ano|findstr {}'


def clearPort(port):
    # 查询指定端口信息
    p1 = subprocess.run(cmd1.format(port), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

    if p1.returncode == 0:
        # 获取进程号
        mat = re.search(' [0-9]{4,5}', str(p1.stdout))
        num = mat.group()
        # 清理进程号
        clear(num)
        print('clear success!')
    else:
        print('no need to clear!')


cmd2 = 'taskkill /pid {} /f'


def clear(port):
    p1 = subprocess.run(cmd1.format(port), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

    if p1.returncode == 0:
        print("清理成功")
    else:
        pass


if __name__ == '__main__':
    clearPort(4723)
