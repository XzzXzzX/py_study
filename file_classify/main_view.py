#!/usr/bin/python
# -*- coding: UTF-8 -*-
# xuan
# 2018-11-26 11:05:41
# 界面显示

# import tkinter
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox 
from file_handle import *

def create_window():
	global window
	window = Tk()
	window.title("文件整理") 		# 设置窗口标题
	window.geometry('600x250') 		# 设置窗口大小
	# window.resizable(width=False, height=True) # 窗口尺寸是否可变，宽可变，高不可变
	window.maxsize(1200, 500) 		# 设置窗口最大尺寸
	window.minsize(600, 250) 		# 最小尺寸
	print("Window size: " + str(window.size))

#
# 初始化界面组件
#
def init_window():
	if window == None:
		print("window is none")
		return
	lab = Label(window, text="输入目录", bg="green", font=("Arial", 12), width=10, height=2, padx=0, pady=0)
	# 打包lab，然后才能显示出来
	lab.pack(side=LEFT) 

	# 创建文本输入框
	# 输入框内容的绑定文本
	window.inputTxt = StringVar()
	entry = Entry(window, width=50, textvariable=window.inputTxt)
	entry.pack()

	# 创建按钮
	# 
	Button(window, text="选择目录", command=click_choose_dic).pack()
	Button(window, text="关闭", command=click_close_btn).pack()
	Button(window, text="开始", command=click_file_handle).pack()

#
# 点击关闭按钮回调
#
def click_close_btn():
	window.quit()

#
# 点击选择目录按钮回调
#
def click_choose_dic():
	ret = filedialog.askdirectory()
	window.inputTxt.set(ret)
	print(str(ret))

#
# 点击选择文件按钮回调
#
def click_choose_file():
	filedialog.askopenfilename()
	

def click_file_handle():
	create_dic(window.inputTxt.get())
	messagebox.showinfo("Tips", "文件整理完成")

def show_window():
	window.mainloop()

if __name__ == '__main__':
	create_window()
	init_window()
	show_window()
	# create_dic("E:/5_my_test_pro/test_py/py_study/py_io")
