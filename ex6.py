# -*- coding: utf-8 -*-

print("수를 입력하세요: ", end="")
a = int(input())

if a > 10:
	if a%2==0 :
		print("10 보다 큰 짝수")
	else:
		print("10 보다 큰 홀수")
elif not a>10:
	if a%2==0 :
		print("10 보다 작은 짝수")
	else:
		print("10 보다 작은 홀수")
else:
	print("이상한 숫자")
