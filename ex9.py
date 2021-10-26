# -*- coding: utf-8 -*-

print("몇 번을 반복할까요? : ", end="")
limit = int(input())

count = limit if limit < 100 else 100

while count>0:
	print("{0}회 반복".format(count))
	count -= 1
	
print("프로그램 종료")
