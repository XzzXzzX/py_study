# -*- coding: utf-8 -*-
#!/usr/bin/env python

# base64相关加解密

import base64


class mybase64(object):
    '''
    base64
    '''

    def __init__(self):
        pass

    def imgToBase64(self, imgPath):
        '''
        图片转base64
        '''
        print("imgTobase64", imgPath)
        f = open(imgPath, 'rb')  # 二进制方式打开图文件
        ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        print(ls_f)

    def base64ToImg(self, base, fileName='img.png'):
        '''
        base64转图片
        '''
        bs = base  # 太长了省略
        imgdata = base64.b64decode(bs)
        file = open(fileName, 'wb')
        file.write(imgdata)
        file.close()

    #
    # 普通文本base64加密 #
    def strToBase64(self, string):
        '''
        普通文本base64加密
        '''
        bs = base64.b64encode(string.encode())
        print(bs.decode())
        return bs.decode()

    #
    # base64加密过的文本，解密成普通文本#
    def base64StrToStr(self, strBase64):
        '''
        base64加密过的文本，解密成普通文本
        '''
        _len = len(strBase64)
        _m = _len % 4
        ex = ''
        if (_m != 0):
            for i in range(4-_m):
                ex += '='
        strBase64 += ex
        data = base64.decodebytes(strBase64.encode('utf-8'))
        print(data.decode())
        return data.decode()
