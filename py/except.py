#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python异常处理

'''
python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误。你可以使用该功能来调试python程序。
异常处理: 。
断言(Assertions):。
'''

try:
	fh = open('testfile','w')
	try:
		fh.write('这是一个测试文件，用于测试异常')
	finally:
		print('最后关闭fh')
		fh.close()
except IOError:
	print('Error:没有找到文件或者读取文件异常')
else:
	print('内容写入文件成功')

# 使用raise 语句手动触发异常
def test_1(level):
	if level < 1:
		raise Exception('Invalid level',level)


try:
	test_1(0)
except Exception:
	print('异常:',Exception.args,1)
else:
	print(2)