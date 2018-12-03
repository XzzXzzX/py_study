#!/usr/bin/python
# -*- coding: UTF-8 -*-
def list_study():
	list1 = [1, 2, 3, 4]
	print("list1: " + str(list1))

	# list *
	print("2 * list1 : " + str(2 * list1))

	# list元素的访问
	print("list1[0]: " + str(list1[0]))

	# 添加元素到list末尾
	list1.append(6)
	print("list1.append(6): " + str(list1))

	# 添加元素到list中
	list1.insert(0, 10)

	# list长度
	print("len(list1): " + str(len(list1)))

	# 判断元素是否存在list中
	ret = 0 in list1
	print("ret : " + str(ret))
	if ret:
		print("0 is in list1")
	else:
		print("0 is not in list1")

	# 统计元素在list中存在多少个
	print("list1.count(1): " + str(list1.count(1)))

	# 切片 [x:y]第(x+1)到第y个元素
	print("list1[1:3]: " + str(list1[1:3]))

 	# 负数 index
	print("list1[-1] : " + str(list1[-1]))


if __name__ == '__main__':
	print("List STUDY")
	list_study()