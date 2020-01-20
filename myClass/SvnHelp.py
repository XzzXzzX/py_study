# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
需要导入svn相关module
下载pysvn，http://pysvn.tigris.org/files/documents/1233/49671/py37-pysvn-svn199-1.9.8-1978-Win64.exe
安装
"""

import os
import sys


class SvnHelp(object):
    """
    svn 命令帮助类

    """

    def __init__(self):
        pass

    def checkout(self, username, svnUrl, targetPath):
        """
        svn checkout 检出  
        username svn账号
        svnUrl svn 地址  
        targetPath 本地目录  
        """
        cmd = 'svn co --username {0} {1} {2}'.format(
            username, svnUrl, targetPath)
        os.popen(cmd)

    def update(self):
        cmd = 'svn up'
        os.popen(cmd)

    def commit(self, msg):
        cmd = 'svn cm -m {0}'.format(msg)
        os.popen(cmd)

    def revert(self):
        cmd = 'svn revert ./'
        os.popen(cmd)


svnHelp = SvnHelp()
