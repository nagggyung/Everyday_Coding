# 미로 탈출
from collections import deque
delta = [[-1,0], [1,0], [0,1], [0,-1]]

def bfs(start):
  y, x = start
  q = deque([start])
  visited[y][x] = 1

  while q:
    y, x = q.popleft()
    for dy, dx in delta:
      ry, rx = y+dy, x+dx

      if ry < 0 or ry > n-1 or rx < 0 or rx > m-1:
        continue
        
      if miro[ry][rx] == 0:
        continue
        
      if miro[ry][rx] == 1:
        q.append([ry, rx])
        miro[ry][rx] = 0
        visited[ry][rx] = visited[y][x] + 1
        

n, m = map(int, input().split())
miro = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
  miro.append(list(map(int, input())))

bfs([0,0])
print(visited[n-1][m-1])

