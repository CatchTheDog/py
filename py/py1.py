#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：py1.py

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
'''
python
多行注释
使用
三个单引号
'''
"""
或者
使用
三个多引号
"""
# 可以使用多行连接符将多行代码连接成为一行
# 在操作符左右都应该有空格
total = "a" + \
    "b" + \
    "c"
print(total)
# 存在[] {} () 时就不需要使用连字符
days = ['a', 'b',
        'd',
        'c']
# 文件最后一行必须以换行符结尾，因为如果不使用换行符结尾，在一些文件操作工具中会引起bug
print(days)




