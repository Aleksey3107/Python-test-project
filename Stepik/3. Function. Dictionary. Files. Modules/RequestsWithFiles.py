import requests

catalog = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_2.txt', 'r') as doc:
	string = doc.readline()

r = requests.get(string)
file = r.text
text = ''

while file[0] != 'We':
	r = requests.get(catalog + file)
	file = r.text
	print(r.url)
	if file.split()[0] == 'We':
		text = r.text
		print(text)
		break
	else:
		continue
