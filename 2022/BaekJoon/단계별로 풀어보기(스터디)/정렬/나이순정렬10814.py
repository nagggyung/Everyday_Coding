num = int(input())
members = []

for _ in range(num):
  age, name = input().split()
  members.append([age, name])

# 나이는 숫자니까 int 로 형 변환 시켜준 뒤 정렬
members.sort(key=lambda x:int(x[0]))

for member in members:
  print(' '.join(map(str, member)))
  