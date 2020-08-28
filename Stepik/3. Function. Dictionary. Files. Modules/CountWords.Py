words = list(i for i in input().lower().split())
counter = dict()

for i in words:
	if i in counter:
		counter[i] += 1
	else:
		counter[i] = 1

for keys, values in counter.items():
	print(keys, values)