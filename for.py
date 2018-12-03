#!/usr/bin/python
# -*- coding: UTF-8 -*-

def test_for():
	list1 = [1, 2, 3, 4, 5]
	for value in list1:
		print(value)
	for index, value in enumerate(list1):
		print(index, value)

	# 画棱形
	width = int(input('输入对角线长度： '))
	print("width: " + str(width))
	for row in range(width + 1):
		# print("row: " + str(row))
		for col in range(width + 1):
			# print("col: " + str(col))
			if ((abs(row - width/2) + abs(col - width/2)) == width/2):
				print("*", end = '')
			else:
				print(" ", end = '')
		print("")

if __name__ == '__main__':
	# test_for()
	print("1")
	print("end")
	print(end = "")
	print("2")
	