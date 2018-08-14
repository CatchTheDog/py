#!/usr/bin/pythin
# -*- coding: UTF-8 -*-

# 面向对象测试

class Employee:
	
	'所有员工的基类'
	
	empCount = 0
	
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		print('父类构造方法')
	
	def displayCount(self):
		print('Total Employee %d' % Employee.empCount)
	
	def dispalyEmployee(self):
		print('Name: ',self.name,',Salary:',self.salary)