# -*- coding: utf-8 -*-
#!/usr/bin/env python

import hashlib


class Md5Helper(object):
    def __init__(self):
        pass

    def get_file_md5(self, file_name):
        """
        计算文件的md5  
        :param file_name:  文件绝对路径
        :return:  md5值
        """
        m = hashlib.md5()  # 创建md5对象
        with open(file_name, 'rb') as fobj:
            while True:
                data = fobj.read(4096)
                if not data:
                    break
                m.update(data)  # 更新md5对象

        return m.hexdigest()  # 返回md5对象

    def get_str_md5(self, content):
        """
        计算字符串md5  
        :param content:  
        :return:  
        """
        m = hashlib.md5(content)  # 创建md5对象
        return m.hexdigest()


# 单例模式
Md5Helper = Md5Helper()
