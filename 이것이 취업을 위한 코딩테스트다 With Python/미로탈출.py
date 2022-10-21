# 이것이 코딩테스트다 chap5 dfs/bfs 

from collections import deque
delta = [[-1,0], [1, 0], [0,-1], [0,1]]

def bfs(start):
    q = deque([start])

    while q:
        y, x = q.popleft()

        for dy, dx in delta:
            tx = x+dx
            ty = y+dy

            if tx < 0 or tx > m-1 or ty < 0 or ty > n-1:
                continue
            if graph[ty][tx] == 1:
                q.append([ty,tx])
                graph[ty][tx] = 0
                visit[ty][tx] = visit[y][x]+1

n, m = map(int, input().split())
graph = []
visit = []


for _ in range(n):
    visit.append([0]*m)
# print(visit)

for _ in range(n):
    graph.append(list(map(int, input())))

graph[0][0] = 0
visit[0][0] = 1

bfs([0,0])
print(visit[n-1][m-1])


