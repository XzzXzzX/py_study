# -*- coding: utf-8 -*-
#!/usr/bin/env python

import threading
import sys
import os


class MobileUtil(object):

    """
    手机端工具方法类
    """

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(self):
        if (not hasattr(MobileUtil, '_instance')):
            with MobileUtil._instance_lock:
                if (not hasattr(MobileUtil, '_instance')):
                    MobileUtil._instance = object.__new__(self)
        return MobileUtil._instance

    def showdevices(self):
        """
        获取已连接的所有设备
        """
        cmd = "adb devices"
        # os.system(cmd)
        ret = os.popen(cmd)
        print(ret)
        # syst
        pass

    def tapscreen(self, pos):
        """
        点击屏幕  
        @pos {x,y} 点击的位置
        """
        cmd = str.format('adb shell input tap {1} {2}', pos.x, pos.y)
        os.popen(cmd)
        pass

    def slicescreen(self, pos1, pos2):
        """
        从pos1滑动到pos2

        """

        pass


# 单例模式
mobileUtil = MobileUtil()

if __name__ == "__main__":
    mobileUtil.showdevices()
