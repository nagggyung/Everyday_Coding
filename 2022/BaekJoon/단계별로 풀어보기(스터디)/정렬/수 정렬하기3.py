
# 백준 수정렬하기 3 10989 
# 계수 정렬(counting sort) 를 이용해서 풀이


import sys

input = sys.stdin.readline
n = int(input())
count = [0]*10001

for _ in range(n):
  count[int(input())] += 1

for i in range(10001):
  for j in range(count[i]):
    print(i)