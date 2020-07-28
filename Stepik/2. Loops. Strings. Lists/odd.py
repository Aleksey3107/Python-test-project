a, b = (int(i) for i in input().split())
count = 0
result = 0


for j in range(a, b + 1):
	if j % 3 == 0:
		result += j
		count += 1

print(result / count)
