# 2. 떡볶이 떡 만들기 

n, m = map(int, input().split())
arr = list(map(int, input().split()))

check_range = [i for i in range(1, max(arr))]
check_range.sort(reverse = True)

for i in range(len(check_range)):
  check = check_range[i]
  tteok = []
  for j in range(len(arr)):
    if arr[j] > check:
      tteok.append(arr[j]-check)

  if sum(tteok) >= m:
    print(check)
    break
      