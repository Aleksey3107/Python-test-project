a = int(input())
b = int(input())
c = int(input())


if a >= b >= c and a >= c:
	print(f'{a}\n{c}\n{b}')
elif a >= c >= b and a >= b:
	print(f'{a}\n{b}\n{c}')
elif b >= a >= c and b >= c:
	print(f'{b}\n{c}\n{a}')
elif b >= c >= a and b >= a:
	print(f'{b}\n{a}\n{c}')
elif c >= b >= a and c >= a:
	print(f'{c}\n{a}\n{b}')
elif c >= a >= b and c >= b:
	print(f'{c}\n{b}\n{a}')
