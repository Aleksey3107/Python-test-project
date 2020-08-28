result_sum = 0
result_sqrt = 0

while True:
	num = int(input())
	result_sum += num
	result_sqrt += num * num
	if result_sum == 0:
		break

print(result_sqrt)
