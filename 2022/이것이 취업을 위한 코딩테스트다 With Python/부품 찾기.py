# chap7. 이진탐색
# 문1. 부품 찾기

def binary_search(arr, target, start, end):
  if start > end:
    return 'no'
  middle = (start + end)//2
  if arr[middle] == target:
    return 'yes'
  elif arr[middle] < target:
      return binary_search(arr, target, middle+1, end)
  else:
      return binary_search(arr, target, start, middle-1)
    
n = int(input())
store = list(map(int, input().split()))
store.sort()

m = int(input())
order = list(map(int, input().split()))

answer = []

for item in order:
  answer.append(binary_search(store, item, 0, len(store)-1))

for i in range(m):
  print(answer[i], end=' ')
