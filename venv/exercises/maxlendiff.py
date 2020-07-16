def mxdiflg(a1, a2):
		result = []
		for i in a1:
				for j in a2:
						result.append(len(i) - len(j))

		return result


print(mxdiflg(
		["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],
		["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))
