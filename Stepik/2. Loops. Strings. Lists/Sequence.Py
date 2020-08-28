string = list(input())
counter = 0
result = []

for i in string:
	if counter == 0:
		result.append(i)
		counter += 1
		result.append(1)
	else:
		if i == result[-2]:
			result[-1] += 1
		else:
			result.append(i)
			result.append(1)

for i in result:
	print(i, end='')
