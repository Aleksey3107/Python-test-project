count_num_one = int(input())
num_one = set(map(int, (input().split())))

count_num_two = int(input())
num_two = set(map(int, (input().split())))

difference = sorted(num_one.symmetric_difference(num_two))

for i in difference:
	print(i)
