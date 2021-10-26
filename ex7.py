# -*- coding: utf-8 -*-

print("요일(월~일)을 입력하세요: ", end="")
day = input()

if day == "월":
	print("Monday")
elif day == "화":
	print("Tuesday")
elif day == "수":
	print("Wednesday")
elif day == "목":
	print("Thursday")
elif day == "금":
	print("Friday")
elif day == "토":
	print("Saturday")
elif day == "일":
	print("Sunday")
else:
	print("잘못된 입력입니다.")
