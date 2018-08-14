#!/usr/bin/python
# -*- coding: UTF-8 -*-

from py.oo.employee import Employee
from py.oo.teacher import Teacher


def printE(emp1,emp2):
	emp1.dispalyEmployee()
	emp2.dispalyEmployee()

emp1 = Employee('Zara',2000)
emp2 = Employee('Manni',5000)

printE(emp1,emp2)

# 为类的实例添加属性
emp1.age = 7
emp2.age = 8

print(emp1.age)
print(emp2.age)

# 删除实例属性
# del emp1.age
# print(emp1.age)

printE(emp1,emp2)

# 获取实例属性
print(hasattr(emp1,'age'))
print(getattr(emp2,'name'))
print(setattr(emp1,'height','10'))
print(delattr(emp1,'height'))



# Employee.displayCount() # 如何定义类的静态方法，如果调用类的静态方法
emp1.displayCount()


# python 类内置属性
print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__class__)

# 继承测试
emp3 = Teacher('Peter',1000,1.8)
emp3.displayCount()
emp3.dispalyEmployee()
emp3.slefDescription()
