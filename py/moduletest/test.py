#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 模块导入，一个模块只会被导入一次 import 模块名；使用:模块名.函数（...）
import support
# from import 可以导入指定模块执行部分，也可以使用*将所有内容全部导入
from math import *

support.print_func('world!')

'''
import python对导入内容的搜索路径：
	1、当前目录
	2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
	3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
'''

'''
命名空间和作用域：
	使用 global varname 表达式可以解决局部变量覆盖全局变量的问题
'''

'''
dir()
    函数一个排好序的字符串列表，内容是一个模块里定义过的名字。返回的列表容纳了在一个模块里定义的所有模块，变量和函数
globals() 和 locals()
	根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
	如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
	如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
	两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。
reload() 函数
	重新执行模块里顶层部分的代码，可以用 reload() 函数,重新导入之前导入过的模块
'''

'''
关于python包：
	包文件夹下必须包含_init_.py文件，该文件内容可以为空；_init_.py用于标识当前文件夹是一个包

'''
