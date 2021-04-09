import uiautomator2 as u
import time
import os

'''
 *
 * @脚本描述: 压力测试设备中心页和支持的设备页之间的跳转50次
 * @编写人: 周鸿炜80244628
 * @创建时间: 2021/04/08
 * @脚本备注:
 * @前置条件: 安装我的设备apk
 * @测试步骤: 进入设备中心，点击'查看支持的设备'，再点击左上角的返回按钮
 * @预期结果: 我的设备apk不会出现奔溃，卡顿的情况
'''

if __name__ == '__main__':
    d=u.connect_usb()
    d.healthcheck()
    d.make_toast("Test Begin",1)
    time.sleep(2)
    os.system("adb shell input swipe 700 2921 700 900")
    time.sleep(2)
    os.system("adb shell am start com.heytap.mydevices/.deviceui.devicecard.DeviceCardHomeActivity")
    for i in range(50):
        '''点击查看支持的设备进入支持的设备页'''
        #d(text="查看支持的设备").click()

        os.system("adb shell input tap 1277 251")
        d(text="查看支持的设备").click()
        os.system("adb shell input tap 99 221")
        print(i)
