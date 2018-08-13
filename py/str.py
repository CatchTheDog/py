#!/usr/bin/python
# -*- coding: UTF-8 -*-
s = 'abcdefg'
print(s[0:5])
print(s[4:])
print(s[-6:-2])
print(s[3])
print(s[:-1])
print(s[:])
print(s[-2:-1])
print(s*2)
print(s + "N")
'''
python的字串列表有2种取值顺序:
从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
如果你要实现从字符串中获取一段子字符串的话，
可以使用 [头下标:尾下标] 来截取相应的字符串，
其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
[头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。
'''

# python 字符串更新
var1 = 'Hello World!'
print('更新字符串：-', var1[: 6] + 'Runoob')

# python转义字符同java,其他字符同普通字符输出
print('\z')
print('\'')

# python 字符串运算符： +  *   [index] [index1:index2] in not in r/R %
print('p' in 'python')
print('x' not in 'python')
print(r'\n')
print(R'\'')

print('My name is %s and weight is %d kg!' % ('zara',21))

'''
python中三引号可以将复杂的字符串进行复制:
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。
三引号实现所见即所得
'''
"""
一对连续的双引号
"""

hi = '''hi
there'''
print(repr(hi))
print(str(hi))

# unicode字符
s = u'Hello\u0020world!'
print(s)

# python字符串内建函数  再联系

