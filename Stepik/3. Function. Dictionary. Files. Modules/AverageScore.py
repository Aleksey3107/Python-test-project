scores = list()

with open('dataset_3363_4.txt', 'r') as doc:
	for i in doc:
		scores.append(i.replace('\n', '').split(';'))

for i in scores:
	del i[0]

result = ([[int(s) for s in sublist] for sublist in scores])

for i in scores:
	print((int(i[0]) + int(i[1]) + int(i[2])) / 3)

total = (list(map(sum, zip(*result))))

for i in total:
	print(round(i / len(scores), 9), end=' ')
