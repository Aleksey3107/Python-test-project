data_range = list(int(i) for i in input().split())

for i in range(data_range[2], int(data_range[3] + 1)):
	print('\t', i, end='\t')
	for j in range(data_range[0], data_range[2]):
		print(j)
