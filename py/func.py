#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python 函数

def func_1(para1,para2=0):
	'''测试函数_1'''
	print('测试函数_1')
	return None


def func_2():
	"测试函数_2"
	print('测试函数_2')
	return 0

def func_3():
	"""测试函数_3"""
	print('测试函数_3')

# 不定长参数
def fun_4(arg1,*vartuple):
	'测试函数-4'
	print('测试函数_4')

print(func_1(1,2)) # 必备参数
print(func_1(para2=3,para1=4)) #关键字参数
print(func_1(para1=7)) # 缺省参数，使用参数默认值 para2=0
print(func_2())
print(func_3())
print(fun_4(1)) # 不定长参数
print(fun_4(2,3,4))

# python 中，类型属于对象，变量是没有类型的

'''
关于python方法传值：
	可变类型：传递引用，方法内修改方法外对象，可以影响方法外对象，如：列表，字典
	不可变类型：传递复制的副本，方法内修改方法外对象，不影响方法外对象，如：整数，字符串，元组
'''

"""
关于函数参数：
	必备参数：必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
	关键字参数：关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值；使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
	默认参数：调用函数时，缺省参数的值如果没有传入，则被认为是默认值
	不定长参数：
"""

'''
匿名函数：
	python使用lambda来创建函数：
		lambda只是一个表达式，函数体比def简单很多。
		lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
		lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
		虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''
sum = lambda arg1, arg2: arg1 + arg2
print('相加后的值为：',sum(10, 20))

'''
变量作用域：
	全局变量：定义在函数外，整个程序范围内都可以访问
	局部变量：定义在函数内，只能在函数内部访问
'''

total = 0
def sum(arg1,arg2):
	total = arg1 + arg2
	print('函数内部局部变量total:',total)
	return total

sum(10,20)

print('函数外部total:',total)