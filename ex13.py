# -*- coding: utf-8 -*-

cnt = 0;
while True:
	cnt += 1
	if cnt==100:
		print("{0}이 되었습니다. 반복문을 종료합니다.".format(cnt))
		break
	elif cnt%3==0:
		continue
		
	print("A {0}".format(cnt))
