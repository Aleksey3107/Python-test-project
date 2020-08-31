result = list()
counter = dict()


with open('dataset_3378_2(1).txt', 'r') as doc:
	for line in doc.readlines():
		result += line.strip().lower().split()

for i in result:
	if i not in counter:
		counter[i] = 1
	else:
		counter[i] += 1

max_counter = max(counter, key=counter.get)
print(f'{max_counter} {counter[max_counter]}')
