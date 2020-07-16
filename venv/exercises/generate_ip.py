def generate_ipv4_list():
		first = 0
		result = []
		while first < 1:
				first += 1
				second = 0
				while second < 78:
						second += 1
						third = 0
						fourth = 0
						while third < 255:
								third += 1
								fourth = 1
								while fourth < 255:
										result.append(f'{first}.{second}.{third}.{fourth}')
										fourth += 1
						result.append(f'{first}.{second}.{third}.{fourth}')
		return result


ips = generate_ipv4_list()


def write_ips(doc):
		i = 1
		file = open("ipv4_addresses.txt", "w+")
		for j in doc[0:5000000]:
				file.write(f'{i};{j}\n')
				i += 1
		file.close()


write_ips(ips)
