#!usr/bin/python
# -*- coding: UTF-8 -*-

# 字典无序，键值对
dic = {'a': 3, 'b': 4}
print(dic)
print(dic['a'])
print(dic.keys())
print(dic.values())

# 修改字典
dic['a'] = 1
dic['b'] = 2
print(dic)

# 删除字典元素
del dic['a']
print(dic)
# del dic
# print(dic)

# 字典值可以是任意类型，但是键：必须唯一，必须不可变（可用字符串，数字或者元组作为键）

# 内置行数&方法
