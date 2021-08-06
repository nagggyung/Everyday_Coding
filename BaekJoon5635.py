n = int(input())
students = []
for i in range(n):
    student = input().split(' ')
    student[1:] = map(int, student[1:])
    students.append(student)

students.sort(key = lambda student: (student[3], student[2], student[1]))
print(students[-1][0])
print(students[0][0])
