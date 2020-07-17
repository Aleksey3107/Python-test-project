import random


def generate_ipv4_list():
	data = set()
	while len(data) <= 5000000:
		data.add('.'.join('%s' % random.randint(0, 256) for i in range(4)))
	return data


ips = generate_ipv4_list()


def write_ips(doc):
	i = 1
	file = open("ipv4_addresses.txt", "w+")
	for j in doc:
		file.write(f'{i};{j}\n')
		i += 1
	file.close()


write_ips(ips)
