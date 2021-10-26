# -*- coding: utf-8 -*-

cnt = 30
half = int( (cnt+1)/2 )

for i in range(cnt):
	for j in range( abs(half - i-1) ):
		print("  ", end="")
		
	for j in range( cnt - 2*abs(half-i-1) -1 + cnt%2):
		print(" *", end="")
		
	print()
