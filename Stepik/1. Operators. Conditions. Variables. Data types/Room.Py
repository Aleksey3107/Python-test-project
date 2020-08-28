import math


figure = str(input())

if figure == 'прямоугольник':
	a = int(input())
	b = int(input())
	print(a * b)
elif figure == 'треугольник':
	a = int(input())
	b = int(input())
	c = int(input())
	p = 0.5 * (a + b + c)
	s = math.sqrt(p * (p - a) * (p - b) * (p - c))
	print(s)
elif figure == 'круг':
	r = int(input())
	print((r ** 2) * 3.14)
