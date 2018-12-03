#!/usr/bin/python
# -*- coding: UTF-8 -*-

from enum import Enum, unique


def enum_normal():
	Mouth = Enum('Mouth', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
	print(Mouth)
	for name, member in Mouth.__members__.items():
		print(name, "==>", member, ", ", member.value)

# @unique装饰器可以帮助我们检查保证没有重复值
# 
@unique
class Weekday(Enum):
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

def test_enumclsaa():
	d1 = Weekday.Mon
	print(d1)

	print(Weekday.Tue)

	print(Weekday['Wed'])

	print(Weekday.Thu.value)

	print(Weekday(1))


if __name__ == '__main__':
	enum_normal()
	test_enumclsaa()