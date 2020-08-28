import requests

result = list()

with open('dataset_3378_2(1).txt', 'r') as doc:
	address = doc.readline().strip()

r = requests.get(address)

print(len(r.text.splitlines()))