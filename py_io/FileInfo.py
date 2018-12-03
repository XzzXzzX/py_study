#!/usr/bin/python
# -*- encoding: UTF-8 -*-
# 
# 
# 
import os, sys
import os.path as Path
import time

def getPath():
	filePath = __file__
	print("当前文件绝对路径： " + filePath)

	realPath = Path.realpath(__file__)
	print("当前文件绝对路径： " + realPath)

	dirName = Path.dirname(realPath)
	print("当前文件目录路径： " + dirName)

	createTime = str(Path.getctime(filePath))
	print("当前文件信息： " + str(Path.getctime(filePath)))


	strs = createTime.split('.')
	print("strs: " + str(strs))
	createTime = strs[0]
	localTime = time.localtime(int(createTime))
	strTime = showtime(int(localTime))
	# strTime = time.ctime(int(createTime))
	print("创建时间： " + strTime)

def showtime(timeStamp):
	timeStruct = time.localtime(int(timeStamp))
	return time.strftime(timeStruct)

if __name__ == '__main__':
	print("main()")
	getPath()