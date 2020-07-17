def generate_ipv4_list():
	first_el = 0
	result = []
	while first_el < 1:
			first_el += 1
			second_el = 0
			while second_el < 78:
					second_el += 1
					third_el = 0
					fourth_el = 0
					while third_el < 255:
							third_el += 1
							fourth_el = 1
							while fourth_el < 255:
									result.append(f'{first_el}.{second_el}.{third_el}.{fourth_el}')
									fourth_el += 1
					result.append(f'{first_el}.{second_el}.{third_el}.{fourth_el}')
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
