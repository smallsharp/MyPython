###1. �鿴ָ��Ӧ�õ�packageName,activity

+ ��ʽ1��<br>
`adb logcat -c`<br>
`adb logcat | findstr "action.Main`

+ ��ʽ2���鿴��ǰҳ�棩��<br>
`adb shell "dumpsys activity activities | grep mFocusedActivity"`

+ ��ʽ3���鿴��ǰҳ�棩��<br>
`adb shell dumpsys window w |findstr \/ |findstr name=`

+ ��ʽ4(�������л���aapt.exe����Ŀ¼ִ�У���sdk\builds-tools\��)��<br>
`aapt dump xmltree xxx.apk AndroidManifest.xml`

###2. ��ȡ��Ļ�ֱ���
adb shell wm size

###3.����ָ��Ӧ�õ���־

ͨ��Ӧ�ð����ƣ����ҵ�����ID�������е���ֵΪ����ID
adb logcat *:I| findstr com.tude.android.template

ͨ������ID������Ӧ�õ���־��Ϣ
adb logcat *:I | findstr "1119"