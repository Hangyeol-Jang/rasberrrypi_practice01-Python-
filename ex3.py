# -*- coding: utf-8 -*-

import sys
print("Please, Input Number: ",end="")
a = int(input())

if a==0:
	print("0 cannot be used for division")
	sys.exit(0)

print("3 /",a,"=",3/a)
