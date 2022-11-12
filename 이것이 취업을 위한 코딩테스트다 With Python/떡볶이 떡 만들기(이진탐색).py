# 떡볶이 떡 만들기
# 이진 탐색으로 문제 풀기


def binary_search(order, target, start, end):
  result = 0
  while start <= end:
    total = 0
    middle = (start + end)//2

    for x in order:
      if x > middle:
        total += (x-middle)

    if total < target:
      end = middle-1
    else:
      result = middle
      start = middle + 1
  return result

n, m = map(int, input().split())
order = list(map(int, input().split()))
order.sort()

start, end = 0, max(order)

print(binary_search(order, m, start, end))
