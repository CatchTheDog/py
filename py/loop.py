#!/usr/bin/python
# -*- coding: UTF-8 -*-

# queen problem with recurison

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
	number = numbers.pop()
	if(number % 2 == 0):
		even.append(number)
	else:
		odd.append(number)
print("odd:", odd)
print("even:", even)


i = 1
while i < 10:
	i += 1
	if i % 2 > 0 :
		continue
	print(i)

i = 1
while 1 :
	print(i)
	i += 1
	if i > 10:
		break


# flag = 1
# while flag: print("Given flag is really true!")
# print("Good bye!")


for letter in 'python':
	print("当前字母：", letter)


for index in range(len('python')):
	print("当前字母：", 'python'[index])

# while … else 在循环条件为 false 时执行 else 语句块
# for … else else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样

# continue,break用法同java
# pass 是空语句，是为了保持程序结构的完整性

for letter in 'python':
	if letter == 'h':
		pass
		print('这是pass块')
	print('当前字母：',letter)
print('Good bye!')