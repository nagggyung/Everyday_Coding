n, m = map(int, input().split())

matrix = []
for _ in range(n):
  matrix.append(list(map(int, input().split())))

max = -1
for i in range(n):
  if max < min(matrix[i]):
    max = min(matrix[i])

print(max)