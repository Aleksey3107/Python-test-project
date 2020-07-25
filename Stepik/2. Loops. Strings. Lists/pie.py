first_team = int(input())
second_team = int(input())
i = 2

while (i % first_team != 0) or (i % second_team != 0):
	i += 1

print(i)
