def modify_list(l):
	result = []
	for i in l:
		if i % 2 == 0:
			result.append(int(i / 2))
		else:
			continue
	return result


val = [1, 2, 3, 4, 5, 6]
print(modify_list(val))
