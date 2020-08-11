values = list(int(i) for i in input().split())
value = int(input())
index = 0
ind = []


for i in values:
	if i == value:
		ind.append(index)
		index += 1
	else:
		index += 1


if len(ind) == 0:
	print('Отсутствует')
else:
	for i in ind:
		print(i, end=' ')