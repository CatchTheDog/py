#!usr/bin/python
# -*- coding: UTF-8 -*-
# 元组是只读列表
a = ('runoob', 786, 2.23, 'john', 70.2)
b = (123, 'john')

print(a)
print(a[0])
print(a[1:3])
print(a[-3:-1])
print(a[2:])
print(a[:-2])
print(a + b*2)


# 元组不可以修改，但是可以将两个元组进行合并
print(a + b)

# 元组元素不能删除，但是可以从命名空间中删除整个元组
# del a
# print(a)

# 元组运算同列表

# 无关闭分隔符：任何无符号的对象，以逗号隔开，默认为元组

print('abc','xyz',4)
print('x,y:', 1, 2)