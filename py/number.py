#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python数字是不可变数据类型

import math
import cmath
import random

print('cmath:', dir(cmath))

print('math', dir(math))

var1 = 1
var2 = 10

# python 支持四中不同的数字类型：int,long,float,complex
print(var1)
print(var2)

# 可以使用del删除Number对象引用
# del var1
# print(var1)
# print(var2)

a = 1.0
b = 1
s = {'a' : '1', 'b' : '2'}

print(int(a))
print(float(b))
print(complex(1,2))
print(str(a))
print(repr(b))
print(eval('a+b'))
print(tuple(s))
print(list(s))
print(chr(b))
print(ord('1'))
print(hex(b))
print(oct(b))

print(cmath.sqrt(-1))
print(cmath.sqrt(9))
print(cmath.sin(1))
print(cmath.log10(100))

# print(math.sqrt(-1))
print(math.sqrt(9))
print(math.sin(1))
print(math.log10(100))

print(math.pi)
print(math.e)

print(random.choice(range(10)))
print(random.randrange(1,10,2))
print(random.uniform(0,1000))


