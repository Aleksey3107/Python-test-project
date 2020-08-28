num = int(input())
result = list()
counter = 0
for i in range(1, num + 1):
	result += ([i] * i)

for i in result:
	print(i, end=' ')
	counter += 1
	if counter == num:
		break
	else:
		continue
