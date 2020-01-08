#-*- coding: utf-8 -*-
#!/usr/bin/env python

# 文件复制、删除

import sys, os, shutil

class myfileopt(object):
    def __init__(self):
        pass
    
    # 
    # 复制文件，非递归#
    # @source_path 源目录
    # @dest_path 目标目录
    # @except_dirs 要排除复制的目录（源目录下的子目录名）
    # @except_files 要排除复制的文件（源目录下的子文件名） #
    def copy_file(self, source_path, dest_path, except_dirs=[], except_files=[]):
        if (not os.path.exists(source_path)):
            print('原路径不存在：', source_path)
        if (not os.path.exists(dest_path)):
            os.makedirs(dest_path)
            print('生成目标路径：', dest_path)

        # 修正要排除的内容 source_path + 对应目录、文件相对路径名
        for i, val in enumerate(except_dirs):
            except_dirs[i + 1] = os.path.join(source_path, val)

        for j, val in enumerate(except_files):
            except_files[j + 1] = os.path.join(source_path, val)

        _files_list = os.listdir(source_path)
        for file_name in _files_list:
            _fix_source = os.path.join(source_path, file_name)
            _fix_dest = os.path.join(dest_path, file_name)
            is_dir = os.path.isdir(_fix_source)
            # print('file_name: ', file_name, is_dir)
            if (is_dir):
                if (_fix_source not in except_dirs):
                    # copy_file(_fix_source, _fix_dest)
                    shutil.copytree(_fix_source, _fix_dest)
                    print('复制目录: ', _fix_source, _fix_dest)
            else:
                if (_fix_source not in except_files):
                    shutil.copy(_fix_source, _fix_dest)
                    print('复制文件: ', _fix_source, _fix_dest)

    # 
    # 删除文件，非递归#
    # @dest_path 目标目录
    # @except_dirs 要排除删除的目录（源目录下的子目录名）
    # @except_files 要排除删除的文件（源目录下的子文件名）
    #  #
    def del_files(self, dest_path, except_dirs=[], except_files=[]):
        _file_list = os.listdir(dest_path)
	
        for _name in _file_list:
            _fix_file = os.path.join(dest_path, _name)
            if (os.path.isdir(_fix_file)):
                if (_fix_file not in except_dirs):
                    shutil.rmtree(_fix_file)
                    print("删除目录：", _fix_file)
                    # del_files(_fix_file, except_files)
            else:
                if (_fix_file not in except_files):
                    os.remove(_fix_file)
                    print("删除文件：", _fix_file)

    def show(self):
        print('show')


import ctypes
from win10toast import ToastNotifier
def send_windows(exStr=''):
	# # 弹窗
	# ctypes.windll.user32.MessageBoxA(0, "msg", "Title", 0)

	# win10推送消息
	toaster = ToastNotifier()
	toaster.show_toast(title=u'客户端更新', msg=u'LYJ_B，测试客户端更新完成\n'+exStr, duration=100)

if __name__ == "__main__":
    # fileopt = myfileopt()
    # fileopt.show()
    send_windows()