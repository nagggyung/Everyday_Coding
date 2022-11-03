n, k = map(int, input().split())

count = 0

count += (n%k)
n = n-(n%k)

while n > 1:
  count += 1
  n = n//k

print(count)
  