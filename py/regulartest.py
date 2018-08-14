#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
python 正则表达式：re模块，提供Perl风格的正则表达式模式。
'''

import re

print(re.match('www','www.baidu.com').span())
print(re.match('com','www.baidu.com'))

line = 'Cats are smarter than dogs'
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matchObj:
	print('matchObj.group():',matchObj.group())
	print('matchObj.group(1):',matchObj.group(1))
	print('matchObj.group(2):',matchObj.group(2))
else:
	print('No match!')
	
searchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)
if matchObj:
	print('searchObj.group():',matchObj.group())
	print('searchObj.group(1):',matchObj.group(1))
	print('searchObj.group(2):',matchObj.group(2))
else:
	print('Nothing found!')

'''
re.match re.search 区别:
	re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
'''

matchObj = re.match(r'dogs',line,re.M|re.I)
if matchObj:
	print('match --> matchObj.group() :',matchObj.group())
else:
	print('No match!')

searchObj = re.search(r'dogs',line,re.M|re.I)
if searchObj:
	print('search --> searchObj.group():',searchObj.group())
else:
	print('Nothing found!')


# 检索和替换

phone = '2004-959-559'

num = re.sub(r'#.*$','',phone)
print('电话号码是：',num)

num = re.sub(r'\D','',phone)
print('电话号码是：',num)

# 传入函数
def double_1(matched):
	value = int(matched.group('value'))
	return str(value*2)

s='A23G4HFD567'
print(re.sub('(?P<value>\d+)',double_1,s))

'''
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，
		供 match() 和 search() 这两个函数使用。
语法格式为：
	re.compile(pattern[, flags])
参数：
	pattern : 一个字符串形式的正则表达式
	flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
		re.I 忽略大小写
		re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
		re.M 多行模式
		re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
		re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
		re.X 为了增加可读性，忽略空格和 # 后面的注释
'''

pattern = re.compile(r'\d+')
m = pattern.findall('one12two2312thre4234e34four')
print(m)
'''
在上面，当匹配成功时返回一个 Match 对象，其中：
group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))。
'''

# match,search 匹配一次，但是findall匹配所有

it = re.finditer(r'\d+','12dfsda232334fdsdf45343123fssr2134')
for match in it:
	print(match.group())

# re.split
# 正则表达式对象
'''
re.compile 返回RegexObject对象
re.MatchObject group返回被RE匹配的字符串
'''

