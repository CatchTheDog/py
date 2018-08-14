#!/usr/bin/python
# -*- coding: UTF-8 -*-
from py.oo.employee import Employee


class Teacher(Employee):
	'''
	Teacher继承Employee，扩展其构造函数，增加一些方法，并重写一些方法
	'''
	def __init__(self,name,salary,height):
		super(Teacher,self).__init__(name,salary)
		self.height = height
		print('子类构造方法')
	
	def dispalyEmployee(self):
		print('Name: ', self.name, ',Salary:', self.salary,',Height:',self.height)
	
	def slefDescription(self):
		print('I am the tearcher!')
		