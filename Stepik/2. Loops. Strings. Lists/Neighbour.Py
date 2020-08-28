a = [int(i) for i in input().split()]
b = []
index = 0

if len(a) > 1:
	for i in a:
		if index == 0:
			b.append(a[index - 1] + a[index + 1])
			index += 1
		elif index == len(a) - 1:
			b.append(a[-2] + a[0])
			index += 1
		elif index < len(a) - 1:
			b.append(a[index - 1] + a[index + 1])
			index += 1
elif len(a) == 1:
	b = a


for j in b:
	print(j, end=' ')
