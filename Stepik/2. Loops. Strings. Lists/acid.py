acid = input().lower()
result = 0

result += acid.count('c')
result += acid.count('g')

print(result / len(acid) * 100)