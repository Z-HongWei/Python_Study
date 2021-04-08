import uiautomator2 as u
import os

if __name__ == '__main__':
    d=u.connect_usb()
    d.healthcheck()
    d.make_toast("Test Begin",1)
    os.system("adb shell input swipe 700 2921 700 900")
    os.system("adb shell am start com.heytap.mydevices/.deviceui.devicecard.DeviceCardHomeActivity")
    for i in range(6):
        '''点击查看支持的设备进入支持的设备页'''
        d(text="查看支持的设备").click()
        os.system("adb shell input tap 99 221")