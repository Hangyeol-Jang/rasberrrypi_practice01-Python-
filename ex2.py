# -*- coding: utf-8 -*-

print("첫 번째 수를 입력하세요: ", end="")
a = input()
print("입력받은 값 : ",a)

print("두 번째 수를 입력하세요: ", end="")
b = input()
print("입력받은 값 : ",a,b)

print("세 번째 수를 입력하세요: ", end="")
c = input()
print("입력받은 값 : ",a,b,c)

print()

result = int(a) * int(b)
#result = a * b # ERROR !!!
print("result : ", result)
print("{0} *  {1} = {2}".format(a, b, result))
