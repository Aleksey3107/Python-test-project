first_num = int(input())
second_num = int(input())
results = divmod(first_num, second_num)

for result in results:
	print(result)

print(results)