count_students_eng = int(input())
students_eng = set(map(int, (input().split())))

count_students_fr = int(input())
students_fr = set(map(int, (input().split())))

print(len(students_eng.union(students_fr)))
