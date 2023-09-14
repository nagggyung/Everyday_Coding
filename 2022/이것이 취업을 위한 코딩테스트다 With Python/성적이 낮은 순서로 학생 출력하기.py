# 성적이 낮은 순서로 학생 출력하기 

n = int(input())
arr = []

for _ in range(n):
  arr.append(list(input().split()))

arr.sort(key=lambda x:x[1])
for i in range(n):
  print(arr[i][0], end = ' ')rr