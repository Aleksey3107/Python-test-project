num = str(input())
first_part = 0
second_part = 0

for i in num[0:3]:
	first_part += int(i)

for j in num[3::]:
	second_part += int(j)


if first_part == second_part:
	print('Счастливый')
else:
	print('Обычный')
