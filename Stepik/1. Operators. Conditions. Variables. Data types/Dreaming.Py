a = int(input("Столько стоит спать: "))
b = int(input("Столько нельзя спать: "))
h = int(input("Столько спит: "))

if a <= h <= b:
	print("Это нормально")
elif h < a:
	print("Недосып")
elif h > b:
	print("Пересып")

