# -*- coding: utf-8 -*-

# 연습문제1 : 1~100 수의 합을 구하시오
sum = 0;
for i in range(100):
	sum += i+1

print("결과 = {0}".format(sum))
print()

# 연습문제2 : 1~100 짝수를 분류하시오
sum = 0;
for i in range(1,101):
	if i%2==0:
		print(i)
	
print()

# 연습문제3 : 1~100 짝수의 합을 구하시오
sum = 0;
for i in range(1,101):
	if i%2==0:
		sum += i

print("결과 = {0}".format(sum))
print()
