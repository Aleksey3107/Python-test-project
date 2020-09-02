verified = list()
for i in range(int(input())):
	verified.append(str(input().lower()))

to_check = set()
for j in range(int(input())):
	string = str(input()).lower().split()
	for i in string:
		to_check.add(i)

distinct = to_check.difference(verified)

for i in distinct:
	print(i)
