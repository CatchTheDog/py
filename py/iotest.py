#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# python io

# 打印到屏幕
print('打印到屏幕测试！')

# 读取键盘输入
'''
Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：
raw_input  从标准输入读取一行，并返回一个字符串，去掉结尾的换行符   已经被抛弃
input 同raw_input,但是它可以接收一个Python表达式作为输入，并将运算结果返回
'''
str = input('请输入：')
print('你输入的内容是：',str)

# 打开或者关闭文件
'''
首先，使用内置函数open打开一个文件，创建一个file对象，然后使用file对象的方法操作此文件即可
'''
fo = open('../README','r+')
print('文件名：',fo.name)
print('是否已经关闭：',fo.closed)
print('访问模式：',fo.mode)
# 向文件中写入中文字符有乱码存在，默认会以GBK写入
str = u'测试file'
fo.write(str.encode('utf-8').decode('utf-8'))
print(fo.read(5))
position = fo.tell()
print('当前指针位置：',position)
print('读取内容：',fo.read(5))
position = fo.seek(0,0)
print('重定位之后读取内容：',fo.read(5))
fo.close()

# python os 模块支持文件的重命名和删除操作

# os.rename('1.txt','iotest.txt')
# os.remove('iotest.txt')

# os模块也支持改变当前目录，创建新目录，删除目录等等
os.chdir('..')
print(os.getcwd())
os.mkdir('iotest')
# os.rmdir('iotest')
