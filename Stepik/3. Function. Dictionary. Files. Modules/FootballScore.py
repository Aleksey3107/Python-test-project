matches_total = list()
teams = set()
table = dict()
for i in range(int(input())):
	name = str(input())
	matches_total.append(name.split(';'))

for match in matches_total:
	teams.add(match[0])
	teams.add(match[2])

for team in teams:
	table[team] = [0, 0, 0, 0, 0]

for i in matches_total:
	if i[0] in table:
		table[i[0]][0] += 1
	if i[2] in table:
		table[i[2]][0] += 1
	if int(i[1]) > int(i[3]):
		table[i[0]][1] += 1
		table[i[0]][-1] += 3
		table[i[2]][3] += 1
	if int(i[1]) < int(i[3]):
		table[i[2]][1] += 1
		table[i[2]][-1] += 3
		table[i[0]][3] += 1
	if int(i[1]) == int(i[3]):
		table[i[2]][2] += 1
		table[i[2]][-1] += 1
		table[i[0]][2] += 1
		table[i[0]][-1] += 1

for q, w in table.items():
	print(q, end=':')
	print(*w)
