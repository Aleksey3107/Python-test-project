strings = []

with open('dataset_3363_3.txt') as doc:
	for i in doc:
		strings.append(i.lower())


for i in strings:
	print((i))