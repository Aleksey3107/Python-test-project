group_size = int(input())
rooms = list(map(int, input().split()))
results = dict()

for i in rooms:
	if i not in results:
		results[i] = 1
	else:
		results[i] += 1

for room, people in results.items():
	if people == 1:
		print(room)
