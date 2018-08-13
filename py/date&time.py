#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import calendar

ticks = time.time()
print('当前事件戳为：',ticks)

# 时间元组
localtime = time.localtime(ticks)
print('本地时间为：',localtime)
print(localtime.tm_year)

# 格式化时间
localtime = time.asctime(localtime)
print('格式化后的时间为：',localtime)

# 2018-08-13 15:45:13
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
# Mon Aug 13 15:46:09 2018
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式化字符串转换为时间
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# 获取某月日历
cal = calendar.month(2016,1)
print('以下输出2016年1月份的日历：')
print(cal)

# cannot import name 'itemgetter' from 'operator' 因为一个本地文件名为operator.py,导致无法使用内置模块中的operator文件
# 将operator.py文件名修改为oper.py后运行程序此异常被修复

# python中，处理日期和时间相关的模块有：time,calendar,datetime,pytz,dateutil等
