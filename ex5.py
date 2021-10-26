# -*- coding: utf-8 -*-

print("수를 입력하세요: ", end="")
a = int(input())

if a > 10 and a%2==0 :
	print("10 보다 큰 짝수")
elif a>10 and a%2==1:
	print("10보다 큰 홀수")
elif a%2==0:
	print("10 이하의 짝수")
else:
	print("10 이하의 홀수")

# Hello World !!! Hello World !!! Hello World !!! Hello World !!!
