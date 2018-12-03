#!/usr/bin/python
# -*- coding: UTF-8 -*-

def tuple_test():
	# 元组在创建的时候就要定义好，因为元组不允许动态修改
	list1 = ['a', 'b']
	tup1 = (1, 2, list1)
	print("tuple dir: ")
	print(dir(tup1))

	# 元组的元素不允许修改，但是如果元组的元素是list，这个list对应的元素是可以修改的
	#  因为元组不改的是元素所指的内存地址，list的操作，不会改变这个list的地址
	#  所以list的改变是允许的
	print("tup1: " + str(tup1))
	print("tuple's address111: ")
	for item in tup1:
		print(id(item))

	tup1[2][1] = 2
	tup1[2].append(3)
	print("tup1: " + str(tup1))
	print("tuple's address222: ")
	for item in tup1:
		print(id(item))

if __name__ == '__main__':
	print(11)
	tuple_test()