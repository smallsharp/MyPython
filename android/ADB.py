'''
Created on 2017年9月29日

@author: cm
'''
import os, subprocess, sys, re, time

dev_list = []


def get_devices():
    devices = []
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    # print(result[1].decode())
    print(len(result))
    if len(result) - 2 == 1:
        for line in result[1:]:
            devices.append(line.strip().decode())
        print(devices[0].split()[0])
        return devices[0].split()[0]
    else:
        print('No device')
        return 'No device found'


def get_pss(devices, pkg_name):
    cmd = "adb -s " + devices + " shell  dumpsys  meminfo %s" % (pkg_name)
    print("cmd:", cmd)
    output = subprocess.check_output(cmd).split()
    # output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    s_men = ".".join([x.decode() for x in output])  # 转换为string
    print("s_men:", s_men)
    men2 = int(re.findall("TOTAL.(\d+)*", s_men, re.S)[0])
    print("men2:", men2)


def mem(device, package):
    cmd = 'adb -s ' + device + ' shell dumpsys meminfo ' + package
    print(cmd)
    res = os.popen(cmd).read()
    part = res[res.find("TOTAL"):res.find("Objects")] # TOTAL   161474   148660     8540        0   175791   160807    14983
    print(part.split()[1])
    return int(part.split()[1])/1024

def mem2(device,package):

    cmd = 'adb -s ' + device + ' shell dumpsys meminfo ' + package
    print(cmd)
    res = subprocess.check_output(cmd).split()
    print(type(res),res)
    res = ".".join([x.decode() for x in res])
    # print(res)
    mem = int(re.findall("TOTAL.(\d+)*", res, re.S)[0])
    print("new:",mem)
    print("-"*100)
    return mem


# def get_battery(devices):
#     cmd = "adb -s " + devices + " shell dumpsys battery"
#     print(cmd)
#     output = subprocess.check_output(cmd).split()
#                stderr=subprocess.PIPE).stdout.readlines()
#     st = ".".join([x.decode() for x in output]) # 转换为string
#     print(st)
#     battery2 = int(re.findall("level:.(\d+)*", st, re.S)[0])
#     writeInfo(battery2, PATH("../info/" + devices + "_battery.pickle"))
#     return battery2


def get_flow(pid, type, devices):
    # pid = get_pid(pkg_name)
    _flow1 = [[], []]
    if pid is not None:
        cmd = "adb -s " + devices + " shell cat /proc/" + pid + "/net/dev"
        print(cmd)
        _flow = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        print(_flow)
        for item in _flow:
            if type == "wifi" and item.split()[0].decode() == "wlan0:":  # wifi
                # 0 上传流量，1 下载流量
                _flow1[0].append(int(item.split()[1].decode()))
                _flow1[1].append(int(item.split()[9].decode()))
                print("------flow---------")
                print(_flow1)
                break
            if type == "gprs" and item.split()[0].decode() == "rmnet0:":  # gprs
                print("-----flow---------")
                _flow1[0].append(int(item.split()[1].decode()))
                _flow1[1].append(int(item.split()[9].decode()))
                print(_flow1)
                break
    else:
        _flow1[0].append(0)
        _flow1[1].append(0)


def get_cpu_kel(devices):
    cmd = "adb -s " + devices + " shell cat /proc/cpuinfo"
    print(cmd)
    output = subprocess.check_output(cmd).split()
    sitem = ".".join([x.decode() for x in output])  # 转换为string
    return len(re.findall("processor", sitem))


'''
 每一个cpu快照均
'''


def totalCpuTime(devices):
    user = nice = system = idle = iowait = irq = softirq = 0
    '''
    user:从系统启动开始累计到当前时刻，处于用户态的运行时间，不包含 nice值为负进程。
    nice:从系统启动开始累计到当前时刻，nice值为负的进程所占用的CPU时间
    system 从系统启动开始累计到当前时刻，处于核心态的运行时间
    idle 从系统启动开始累计到当前时刻，除IO等待时间以外的其它等待时间
    iowait 从系统启动开始累计到当前时刻，IO等待时间(since 2.5.41)
    irq 从系统启动开始累计到当前时刻，硬中断时间(since 2.6.0-test4)
    softirq 从系统启动开始累计到当前时刻，软中断时间(since 2.6.0-test4)
    stealstolen  这是时间花在其他的操作系统在虚拟环境中运行时（since 2.6.11）
    guest 这是运行时间guest 用户Linux内核的操作系统的控制下的一个虚拟CPU（since 2.6.24）
    '''
    cmd = "adb -s " + devices + " shell cat /proc/stat"
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    res = output.split()

    for info in res:
        if info.decode() == "cpu":
            user = res[1].decode()
            nice = res[2].decode()
            system = res[3].decode()
            idle = res[4].decode()
            iowait = res[5].decode()
            irq = res[6].decode()
            softirq = res[7].decode()
            print("user=" + user)
            print("nice=" + nice)
            print("system=" + system)
            print("idle=" + idle)
            print("iowait=" + iowait)
            print("irq=" + irq)
            print("softirq=" + softirq)
            result = int(user) + int(nice) + int(system) + int(idle) + int(iowait) + int(irq) + int(softirq)
            print("totalCpuTime" + str(result))
            return result


'''
每一个进程快照
'''


def processCpuTime(pid, devices):
    '''

    pid     进程号
    utime   该任务在用户态运行的时间，单位为jiffies
    stime   该任务在核心态运行的时间，单位为jiffies
    cutime  所有已死线程在用户态运行的时间，单位为jiffies
    cstime  所有已死在核心态运行的时间，单位为jiffies
    '''
    utime = stime = cutime = cstime = 0
    cmd = "adb -s " + devices + " shell cat /proc/" + pid + "/stat"
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    res = output.split()
    utime = res[13].decode()
    stime = res[14].decode()
    cutime = res[15].decode()
    cstime = res[16].decode()
    print("utime=" + utime)
    print("stime=" + stime)
    print("cutime=" + cutime)
    print("cstime=" + cstime)
    result = int(utime) + int(stime) + int(cutime) + int(cstime)
    print("processCpuTime=" + str(result))
    return result


'''
计算某进程的cpu使用率
100*( processCpuTime2 – processCpuTime1) / (totalCpuTime2 – totalCpuTime1) (按100%计算，如果是多核情况下还需乘以cpu的个数);
cpukel cpu几核
pid 进程id
'''


def cpu_rate(pid, cpukel, devices):
    # pid = get_pid(pkg_name)
    processCpuTime1 = processCpuTime(pid, devices)
    time.sleep(1)
    processCpuTime2 = processCpuTime(pid, devices)
    processCpuTime3 = processCpuTime2 - processCpuTime1

    totalCpuTime1 = totalCpuTime(devices)
    time.sleep(1)
    totalCpuTime2 = totalCpuTime(devices)
    totalCpuTime3 = (totalCpuTime2 - totalCpuTime1) * cpukel

    cpu = 100 * (processCpuTime3) / (totalCpuTime3)
    print(cpu)


# def get_fps(pkg_name, devices):
#     _adb = "adb -s " + devices + " shell dumpsys gfxinfo %s" % pkg_name
#     print(_adb)
#     results = os.popen(_adb).read().strip()
#     frames = [x for x in results.split('\n') if validator(x)]
#     frame_count = len(frames)
#     jank_count = 0
#     vsync_overtime = 0
#     render_time = 0
#     for frame in frames:
#         time_block = re.split(r'\s+', frame.strip())
#         if len(time_block) == 3:
#             try:
#                 render_time = float(time_block[0]) + float(time_block[1]) + float(time_block[2])
#             except Exception as e:
#                 render_time = 0
# 
#         '''
#         当渲染时间大于16.67，按照垂直同步机制，该帧就已经渲染超时
#         那么，如果它正好是16.67的整数倍，比如66.68，则它花费了4个垂直同步脉冲，减去本身需要一个，则超时3个
#         如果它不是16.67的整数倍，比如67，那么它花费的垂直同步脉冲应向上取整，即5个，减去本身需要一个，即超时4个，可直接算向下取整
# 
#         最后的计算方法思路：
#         执行一次命令，总共收集到了m帧（理想情况下m=128），但是这m帧里面有些帧渲染超过了16.67毫秒，算一次jank，一旦jank，
#         需要用掉额外的垂直同步脉冲。其他的就算没有超过16.67，也按一个脉冲时间来算（理想情况下，一个脉冲就可以渲染完一帧）
# 
#         所以FPS的算法可以变为：
#         m / （m + 额外的垂直同步脉冲） * 60
#         '''
#         if render_time > 16.67:
#             jank_count += 1
#             if render_time % 16.67 == 0:
#                 vsync_overtime += int(render_time / 16.67) - 1
#             else:
#                 vsync_overtime += int(render_time / 16.67)
# 
#     _fps = int(frame_count * 60 / (frame_count + vsync_overtime))
# 
#     # return (frame_count, jank_count, fps)
#     print("-----fps------")
#     print(_fps)


if __name__ == '__main__':
    #     get_flow("10138", 'wifi', "06694a9b006097fb");
    # get_pss("85GBBMA2353T", "com.jingdong.app.mall")
    # get_pss("85GBBMA2353T", "com.tude.android")
    # mems = mem("85GBBMA2353T", "com.jingdong.app.mall")
    mems = mem2("85GBBMA2353T", "com.jingdong.app.mall")
    # print(mems)
    # file = open("men2.txt","w")
    # file.write(mems)
    # file.close()