import sys

input = sys.stdin.readline
num = int(input())
loc = []


for _ in range(num):
  x, y = map(int, input().split())
  loc.append([x,y])

loc.sort(key=lambda x:(x[1],x[0]))

for i in range(len(loc)):
  print(' '.join(map(str,loc[i])))