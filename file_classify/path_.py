import os
import shutil

os.getcwd()  # 获取当前工作目录，非脚本目录
os.listdir()  # 返回指定目录下的所有文件和目录，非递归
os.remove()  # 删除文件
os.removedirs()  #删除目录
os.path.isfile()  # 检验给出的路径是否是一个文件
os.path.isdir()  # 检验给出的路径是否是一个目录
os.path.isabs()  # 判断是否是绝对路径
os.path.exists()  # 检验给出的路径是否真实存在
os.path.split()  # 返回一个路径的目录名和文件名
os.path.splitext()  # 分离文件扩展名
os.path.dirname()  # 获取文件路径名
os.path.basename() # 获取一个绝对路径下的文件名
os.system()  # 运行shell命令
os.rename(old,new) # 重命名文件或目录
os.makedirs(r"c:\python\test")  # 创建多级目录
os.mkdir("test")  # 创建单个目录
os.exit()  # 终止当前进程
os.path.getsize(filename)  # 获取文件大小
os.mknod("test.txt")  # 创建空文件
os.path.join(“home”, "me", "mywork")  # 路径连接


shutil.copyfile("oldfile","newfile")  # oldfile和newfile都只能是文件
shutil.copytree("olddir","newdir")  # olddir和newdir都只能是目录，且newdir必须不存在
shutil.move("oldpos","newpos")  # 移动文件或目录
shutil.rmtree("dir")  # 删除目录，与os.removedirs()相同
# --------------------- 
# 作者：milletluo 
# 来源：CSDN 
# 原文：https://blog.csdn.net/lm409/article/details/75452306 
# 版权声明：本文为博主原创文章，转载请附上博文链接！