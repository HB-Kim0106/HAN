#!/usr/bin/python3

num1 = 21

if num1%3 == 0 and num1%7 != 0:
	print(num1, "은 3의 배수이다.")
elif num1%3 != 0 and num1%7 == 0:
	print(num1, "은 7의 배수이다.")
elif num1%3 == 0 and num1%7 == 0:
	print(num1, "은 3의 배수이고 7의 배수이다.")
else:
	print(num1, "은 3의 배수도 아니고 7의 배수도 아니다.")
