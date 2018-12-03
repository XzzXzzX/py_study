#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 类的定义
# 关键字class，j类名后面()内的是这个类，所继承的对象，默认所有对象都是继承object
# 对于类的方法， 不要忘记self
# 
# 访问限制
# 让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
#
# 对于私有的属性，也可通过 _Student__name来访问，但是强烈不建议这么做，因为不同版本的Python解释器可能会把__name改成不同的变量名
# 
# 

class Student(object):

	"""docstring for Student"""
	def __init__(self, name, score):
		super(Student, self).__init__()
		self.__name = name
		self._score = score

	def print_student(self):
		print("Name: %s" % self.__name, end = ' ')
		print("Score: %d" % self._score)
		print("")

	# def get_grade(self):
	# 	if self.score > 90:
	# 		return 'A'
	# 	elif self.score > 60:
	# 		return 'B'
	# 	else:
	# 		return 'C'

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError("score must be an integer")
		if value < 0 or value > 100:
			raise ValueError("score must between 0~100")
		self._score = value
	

def test_student():
	stu1 = Student("Neee", 80)
	stu1.name = "Naaa"
	stu1.score = 89
	stu2 = Student("Stu2", 90)
	stu_list = [stu1, stu2]
	for stu in stu_list:
		stu.print_student()
	print(stu1._Student__name)
	print(stu1)



#*****************************************************************************************
# 继承
class Animal(object):
	name = "1"
	"""docstring for Animal"""
	def __init__(self):
		super(Animal, self).__init__()
		self.name = "3"

	def eat(self):
		print("Animal eat()")


class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		super(Dog, self).__init__()

class Husky(Dog):
	"""docstring for Husky"""	
	def __init__(self):
		super(Husky, self).__init__()
						
def test_polym():
	a = Animal()
	b = Dog()
	c = Husky()

	print("a is Animal : " + str(isinstance(a, Animal)))
	print("a is Dog : " + str(isinstance(a, Dog)))
	print("a is Husky : " + str(isinstance(a, Husky)))
	print("b is Animal : " + str(isinstance(b, Animal)))
	print("b is Dog : " + str(isinstance(b, Dog)))
	print("b is Husky : " + str(isinstance(b, Husky)))
	print("c is Animal : " + str(isinstance(c, Animal)))
	print("c is Dog : " + str(isinstance(c, Dog)))
	print("c is Husky : " + str(isinstance(c, Husky)))

	# getattr()、setattr()以及hasattr()
	# 获取属性，没有属性则返回第三个参数，
	name = getattr(a, 'name')
	sex = getattr(a, 'sex', None)
	print("getattr: " + str(name))
	print("getattr: " + str(sex))  

	# 判断是否存在此方法或属性
	if hasattr(a, "eat"):
		print("hasattr eat")
		func_eat = getattr(a, 'eat')
		func_eat()
	else:
		print('no attr eat')
	if hasattr(a, 'run'):
		print('hasattr run')
		a.run()
	else:
		print('no attr run')

#********************************************************************************************
#
# 属性限制
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# ****使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的*****
class Base(object):
	__slots__ = ('attr1', 'attr2')
	"""docstring for Base"""
	def __init__(self):
		super(Base, self).__init__()

class Child(Base):
	"""docstring for Child"""
	def __init__(self):
		super(Child, self).__init__()
		

def slots_test():
	# 子类还可以添加属性
	child1 = Child()
	child1.attr = 0
	child1.attr1 = 1

	base1 = Base()
	base1.attr1 = 1
	# 有__slots__的不能再添加属性
	# base1.attr = 0

# ************************************************************************************************
# 定制类。
# 
# 方法链
# 方法链的一个好处，是可以减少你使用对象名的次数。调用的方法越多，能够减少的次数就越多。
# 因此，这个方法也能一定程度上减少需要阅读、测试、调试、维护的代码数量。这个好处不大，但也是有用的。
#请注意，方法链的一个限制是，只能用在不需要返回其他值的方法上，因为你需要返回self对象。
#即使Python支持用一个return语句返回多个值，也可能无法解决这个问题。
class Chain(object):
	def __init__(self, path=""):
		self._path = path

	def __getattr__(self, path):
		return Chain("%s/%s" % (self._path, path))

	def __call__(self, path):
		return Chain("%s/%s" % (self._path, path))

	def __str__(self):
		return self._path

	def func1(self):
		print("func1")
		return self

	def func2(self):
		print("func2")
		return self

	__repr__ = __str__

def test_class():
	ch = Chain()
	print(ch)
	print(Chain().a.b.c.d)
	ch.func1().func2()

# ************************************************************************************************

if __name__ == '__main__':
	test_student()
	test_polym()
	slots_test()
	test_class()