import random
import string


def generate_ipv4_list():
	data = set()
	while len(data) <= 5000000:
		data.add('.'.join('%s' % random.randint(0, 256) for i in range(4)))
		print(len(data))
	return data


def generate_ipv6_list():
	data = set()
	while len(data) <= 5000000:
		data.add("2001:cafe:" + ":".join(("%x" % random.randint(0, 16**4) for i in range(6))))
	return data


# ipv4 = generate_ipv4_list()
ipv6 = generate_ipv6_list()


def write_ipv4(doc):
	i = 1
	file = open("ipv4_addresses.txt", "w+")
	for j in doc:
		file.write(f'{i};{j}\n')
		i += 1
	file.close()


def write_ipv6(doc):
	i = 1
	file = open("ipv6_addresses.txt", "w+")
	for j in doc:
		file.write(f'{i};{j}\n')
		i += 1
	file.close()


# write_ipv4(ipv4)
write_ipv6(ipv6)
