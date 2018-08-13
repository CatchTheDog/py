#!usr/bin/python
# -*- coding: UTF-8 -*-
# python 列表 python有6个序列的内置类型，序列都可以进行索引，切片，加，乘，检查成员
# 列表的数据项不需要具有相同的数据类型

t = ['a', 'b', 'c']
s = ['d', 'e']

# 列表的操作同字符串
print(t[0])
print(t[0: 2])
print(t[-2: -1])
print(t[-3:])
print(t[: -1])
print(t + s * 3)

# 更新列表
s.append('f')
s.append('g')
print(s)

# 删除元素
del s[0]
print(s)

# 与字符串相同，列表也支持 len()  +  *   in  not in

# 列表截取 同字符串 [index1:index2]

# 列表内置函数
print(len(s))
print(max(s))
print(min(s))




