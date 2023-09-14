import collections 
import sys 

# input 시간 초과 발생 막기 위해서는 sys.stdin.readline 사용
input = sys.stdin.readline
n = int(input())
arr = []
sum = 0

for _ in range(n):
  add = int(input())
  sum += add
  arr.append(add)

arr.sort()

# 각 키에대한 빈도 수 확인할 때 Counter dict 사용
counter_arr = collections.Counter(arr)

# most_common(num) 을 사용하면 최빈값을 구할 수 있다. 
# num 의 개수만큼 최빈 값이 큰 순서대로 반환하게 된다.
often_count = counter_arr.most_common(1)[0][1]
often_arr = []

for k, v in counter_arr.items():
  if v == often_count:
    often_arr.append(k)

often_arr.sort()

avg = round(sum/n)
mid = arr[len(arr)//2]
if len(often_arr)>1:
  often = often_arr[1]
else:
  often = often_arr[0]

range = arr[-1]-arr[0]

# result
print(avg)
print(mid)
print(often)
print(range)





