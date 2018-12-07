#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
# xuan
# 2018-11-26 11:36:22
# file_handle.py文件处理
# 

import os, sys
import os.path as Path
import time
import shutil

def is_element_exist(t, element):
	if None == t or None == element :
		return False
	for x in t:
		if x == element:
			return True
	return False

#
# 处理文件及目录
# 
# @dicPath 目录路径
# # copyOrMove 复制操作还是移动操作 False为复制操作，True为移动操作
def create_dic(dicPath, copyOrMove=False):
	fileList = os.listdir(dicPath)
	dateList = []
	fileDic = {}
	print(str(fileList))
	for x in fileList:
		filepath = dicPath + "/" + x
		# 判断是文件
		if Path.isfile(filepath): 
			dataStr = get_format_time(Path.getctime(filepath))
			dicpath = Path.join(dicPath, dataStr) # dicPath + "/" + dataStr 

			# 判断是否已记录
			if not is_element_exist(dateList, dataStr): 
				dateList.append(dataStr)
				# 根据日期创建目录
				dicpath = dicPath + "/" + dataStr
				if not Path.exists(dicpath):
					os.mkdir(dicpath)

			fileDic[filepath] = dicpath
			# 操作文件
			if copyOrMove:
				shutil.move(filepath, Path.join(dicpath, x))
			else:
				shutil.copyfile(filepath, Path.join(dicpath, x))



	print("日期列表： " + str(dateList))

def rename_files(fileList):
	if None == fileList:
		print("fileList is None")
		return

#
#	通过时间戳获取时间日期，取年月日
#
def get_format_time(timeStamp):
	timeStruct = time.localtime(int(timeStamp))
	return time.strftime("%Y-%m-%d", timeStruct)
