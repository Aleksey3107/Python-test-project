first_num = float(input())
second_num = float(input())
operation = str(input())
# do not miss /
if operation == '+':
	print(first_num + second_num)
elif operation == '-':
	print(first_num - second_num)
elif operation == '/' and second_num == 0:
	print("Деление на 0!")
elif operation == '/' and second_num != 0:
	print(first_num / second_num)
elif operation == '*':
	print(first_num * second_num)
elif operation == 'mod' and second_num == 0:
	print("Деление на 0!")
elif operation == 'mod':
	print(first_num % second_num)
elif operation == 'pow':
	print(first_num ** second_num)
elif operation == 'div' and second_num == 0:
	print("Деление на 0!")
elif operation == 'div':
	print(first_num // second_num)
elif operation == '/' and second_num == 0:
	print("Деление на 0!")
