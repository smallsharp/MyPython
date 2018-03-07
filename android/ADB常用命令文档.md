###1. 查看指定应用的packageName,activity

+ 方式1：<br>
`adb logcat -c`<br>
`adb logcat | findstr "action.Main`

+ 方式2（查看当前页面）：<br>
`adb shell "dumpsys activity activities | grep mFocusedActivity"`

+ 方式3（查看当前页面）：<br>
`adb shell dumpsys window w |findstr \/ |findstr name=`

+ 方式4(命令行切换到aapt.exe所在目录执行（在sdk\builds-tools\）)：<br>
`aapt dump xmltree xxx.apk AndroidManifest.xml`

###2. 获取屏幕分辨率
adb shell wm size

###3.过滤指定应用的日志

通过应用包名称，查找到进程ID，第三列的数值为进程ID
adb logcat *:I| findstr com.tude.android.template

通过进程ID，过滤应用的日志信息
adb logcat *:I | findstr "1119"