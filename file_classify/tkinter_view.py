#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from file_handle import *
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('文件整理')
        self.master.geometry('568x117')
        self.master.resizable(width=False, height=False)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.check_box1_val = IntVar()
        self.check_box1_val.set(1)
        self.style.configure('check_move.TRadiobutton',font=('宋体',9))
        self.check_move = Radiobutton(self.top, text='移动文件', value=0, variable=self.check_box1_val, command=self.check_move_Cmd, style='check_move.TRadiobutton')
        self.check_move.place(relx=0.338, rely=0.615, relwidth=0.143, relheight=0.214)

        self.style.configure('check_copy.TRadiobutton',font=('宋体',9))
        self.check_copy = Radiobutton(self.top, text='复制文件', value=1, variable=self.check_box1_val, command=self.check_copy_Cmd, style='check_copy.TRadiobutton')
        self.check_copy.place(relx=0.183, rely=0.615, relwidth=0.143, relheight=0.214)

        self.style.configure('Btn_handle.TButton',font=('宋体',9))
        self.Btn_handle = Button(self.top, text='开始处理', command=self.Btn_handle_Cmd, style='Btn_handle.TButton')
        self.Btn_handle.place(relx=0.775, rely=0.615, relwidth=0.171, relheight=0.282)

        self.style.configure('Btn_open.TButton',font=('宋体',9))
        self.Btn_open = Button(self.top, text='打开目录', command=self.Btn_open_Cmd, style='Btn_open.TButton')
        self.Btn_open.place(relx=0.775, rely=0.205, relwidth=0.171, relheight=0.282)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.183, rely=0.274, relwidth=0.551, relheight=0.214)

        # self.style.configure('Label2.TLabel',anchor='w', font=('宋体',9))
        # self.Label2 = Label(self.top, text='复制/移动', style='Label2.TLabel')
        # self.Label2.place(relx=0.014, rely=0.684, relwidth=0.1, relheight=0.214)

        self.style.configure('Label1.TLabel',anchor='center', foreground='#F4F7FC', background='#B4B4B4', font=('宋体',9))
        self.Label1 = Label(self.top, text='选择目录', style='Label1.TLabel')
        self.Label1.place(relx=0.014, rely=0.274, relwidth=0.127, relheight=0.239)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        # self.isMoveFile = False # 是否是移动文件操作
        # self.isCreateTime = True # 是否是以创建时间为分类

    def check_move_Cmd(self, event=None):
        print("Application.check_move_Cmd()")
        pass

    def check_copy_Cmd(self, event=None):
        print("Application.check_move_Cmd()")
        pass

    def Btn_handle_Cmd(self, event=None):
        print("Application.check_move_Cmd()")
        pass

    def Btn_open_Cmd(self, event=None):
        print("Application.check_move_Cmd()")
        pass

# if __name__ == "__main__":
#     top = Tk()
#     Application(top).mainloop()
#     try: top.destroy()
#     except: pass
