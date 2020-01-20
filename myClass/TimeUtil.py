# -*- coding: utf-8 -*-
#!/usr/bin/env python


class TimeUtil(object):
    def __init__(self):
        pass

    def secondsToStr(self, seconds):
        """
        秒数转str xx小时xx分xx秒

        """
        t_m = 0
        t_h = 0
        if (seconds >= 60):
            t_m = int(seconds / 60)
        if (t_m >= 60):
            t_h = int(t_m / 60)
            t_m = t_m % 60
        seconds = seconds % 60
        if (t_h > 0):
            return str(t_h) + u'小时' + str(t_m) + u'分' + str(seconds) + u'秒'
        if (t_m):
            return str(t_m) + u'分' + str(seconds) + u'秒'
        return str(seconds) + u'秒'


# 单例模式1
timeUtil = TimeUtil()
