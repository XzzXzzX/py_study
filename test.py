# -*- coding: utf-8 -*-
#!/usr/bin/env python

# import pydub.audio_segment as audioMgr
# import ffmpeg
# email 用于构建邮件内容
# 用于构建邮件头
from email.header import Header
from email.mime.text import MIMEText
# smtplib 用于邮件的发信动作
import smtplib
from pydub import AudioSegment
from myClass.TimeUtil import timeUtil
from myClass.Md5Help import Md5Helper

import base64

import os


def testWav(filePath):

    with open(filePath) as f:
        print(dir(f))
        pass
    pass


def testMail():

    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = 'zhangxuan13@qq.com'
    # 'hqixprprqofhbceh'  # 'rbteqaqmgbeubeda'  # 'yavnfxhzysufbfbe'  # 'hqixprprqofhbceh'
    password = 'qkguitvhlqnmbeic'
    # password = base64.b64encode(password.encode()).decode()
    # from_addr = base64.b64encode(from_addr.encode()).decode()

    # 收信方邮箱
    to_addr = '673194747@qq.com'

    # 发信服务器
    smtp_server = "smtp.exmail.qq.com"  # 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText('send by python', 'plain', 'utf-8')

    try:
        # 开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(smtp_server)
        server.set_debuglevel(1)
        server.connect(smtp_server, 465)
        # 登录发信邮箱
        server.login(from_addr, password)

        # 邮件头信息
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('python test')
        # 发送邮件
        server.sendmail(from_addr, to_addr, msg.as_string())
        # 关闭服务器
        server.quit()
        print("邮件发送成功")

    except smtplib.SMTPAuthenticationError:
        print("Error: 无法发送邮件", smtplib.SMTPAuthenticationError)


def testFor():
    s = {"a": 'aa', "b": 'bb'}
    for v in s:
        print('===>%s %s' % (v, s[v]))
    pass


if __name__ == "__main__":
    # wavPath = 'C:\\Users\\User\\Desktop\\temp\\music/01 爱在西元前.wav'
    # song = AudioSegment.from_wav(wavPath)
    # # testWav(wavPath)
    # print(dir(song))
    # print(str(song.channels))
    # testMail()

    print(timeUtil.secondsToStr(3600))
    print('{0} {1}'.format('aaa', 'ccc'))

    dirName = os.path.dirname(__file__)
    print('md5: ' + Md5Helper.get_file_md5(dirName + '/list.py'))
    print('cur time: ' + str(os.path.getmtime(dirName + '/list.py')))
    os.utime(dirName + '/list.py')
    print('cur time11: ' + str(os.path.getmtime(dirName + '/list.py')))

    print('修改时间 md5: ' + Md5Helper.get_file_md5(dirName + '/list.py'))

    # {3, 4, 22, '8', "原生包231", 5, '5-1', '6', '6-1'}
    testList = {3, 4, 22, '8', "原生包231", 5, '5-1', '6', '6-1'}

    # for i, value in enumerate(testList):
    #     print(str(i), str(value))
    testFor()

    pass
