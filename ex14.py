# -*- coding: utf-8 -*-

while True:
	print()
	print("반복을 계속할까요?[예/아니오] : ", end="")
	answer = input()
	if answer=="예":
		print("반복을 계속합니다.")
		continue
	elif answer=="아니오":
		print("반복을 중단합니다.")
		break
	else:
		print("잘못된 입력값입니다.")
	
