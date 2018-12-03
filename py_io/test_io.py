#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
import msvcrt
from io import StringIO


def file_open(file_path):
	if not (os.path.exists(file_path) and os.path.isfile(file_path)):
		print("file_open() file_path有问题： " + file_path)
		return
	#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
	#所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
	# try:
	# 	f = open("test.txt")
	# 	print(f.read())
	# finally:
	# 	if f:
	# 		f.close()

	# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
	with open(file_path, 'r') as f:
		strs = f.read()
		print("【OLD】: " + strs)
		strs.replace("Person", "Human")
		print("【NOW】: " + strs)

def file_write():
	with open('test.txt', 'w+') as f:
		f.write('Hello World!')

def string_io():
	f = StringIO()
	ret = f.write('Hello')
	print('f.write() ret1 : ', ret)
	ret = f.write(' ')
	print('f.write() ret2 : ', ret)
	ret = f.write('World')
	print('f.write() ret3 : ', ret)

	f = StringIO('Hello!\nHi!\nGoodbye!')
	while True:
		s = f.readline()
		if s == '':
			break
		print(s.strip())

def get_file_list_and_show():
	lists = os.listdir()
	print(lists)
	global file_list
	global dir_list
	file_list, dir_list = [], []
	for dir in lists:
		if os.path.isfile(dir):
			file_list.append(dir)
		elif os.path.isdir(dir):
			dir_list.append(dir)
		else:				
			print("unkown path: " + dir)
	
	file_list.sort()
	dir_list.sort()
	print(file_list)
	print(dir_list)


if __name__ == '__main__':

	print("Cur Work Path: " + os.getcwd())
	get_file_list_and_show()

	file_open(file_list[0])
	# file_write()
	# string_io()

	# os.system("pause")
	# 按回车键退出
	# raw_input(unicode('按回车键退出...','utf-8').encode('gbk'))
	ret = msvcrt.getch()
	print("intput char: " + str(ret))
