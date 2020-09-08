# num_testcases = int(input())
for i in range(int(input())):
	num_elements_a = int(input())
	elements_a = set(map(int, input().split()))
	num_elements_b = int(input())
	elements_b = set(map(int, input().split()))
	print(True) if elements_a.issubset(elements_b) else print(False)
