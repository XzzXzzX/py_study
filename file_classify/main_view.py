#!/usr/bin/python
# -*- coding: UTF-8 -*-
# xuan
# 2018-11-26 11:05:41
# main_view.py 界面显示

from tkinter_view import *
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog

class MainView(Application):
	"""docstring for MainView"""
	def __init__(self, view):
		super(MainView, self).__init__(view)
		self.isMoveFile = False # 是否是移动文件操作
		self.isCreateTime = True # 是否是以创建时间为分类
		
	def check_move_Cmd(self, event=None):
		print("MainView.check_move_Cmd()")
		self.isMoveFile = True
		pass

	def check_copy_Cmd(self, event=None):
		print("MainView.check_copy_Cmd()")
		self.isMoveFile = False
		pass

	def Btn_handle_Cmd(self, event=None):
		print("MainView.Btn_handle_Cmd()")
		self.isMoveFile = self.isMoveFile or False
		create_dic(self.Text1Var.get(), self.isMoveFile)
		messagebox.showinfo("Tips", "文件整理完成")

	def Btn_open_Cmd(self, event=None):
		print("MainView.Btn_open_Cmd()")
		self.Text1Var.set(filedialog.askdirectory())
		pass
		

if __name__ == '__main__':
	top = Tk()
	MainView(top).mainloop()
	try: top.destroy()
	except: pass
	# create_dic("E:/5_my_test_pro/test_py/py_study/py_io")
