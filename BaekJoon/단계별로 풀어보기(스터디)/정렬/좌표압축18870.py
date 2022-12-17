import collections

num = int(input())
arr = list(map(int, input().split()))
set_arr = sorted(list(set(arr)))

dict = collections.defaultdict(int)

for idx, v in enumerate(set_arr):
  dict[v] = idx

for num in arr:
  if num in dict:
    print(dict[num], end=' ')
