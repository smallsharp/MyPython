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

###3.