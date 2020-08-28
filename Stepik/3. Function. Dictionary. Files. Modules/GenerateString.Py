with open('dataset_3363_2.txt', 'r') as doc:
	string = doc.readline()

result = []
counter = 0

for i in string:
	if i != '\n':
		if not string[counter].isnumeric():
			result.append(i)
			counter += 1
		elif string[counter].isnumeric() and string[counter - 1].isnumeric():
			result[-1] = int(str(result[-1]) + str(string[counter]))
			counter += 1
		elif string[counter].isnumeric() and not string[counter - 1].isnumeric():
			result.append(int(i))
			counter += 1
	else:
		break

final_string = ''
index = 0
for i in result:
	if index != len(result) - 2:
		final_string += result[index] * int(result[index + 1])
		index += 2
	else:
		final_string += result[index] * int(result[index + 1])
		break

print(final_string)