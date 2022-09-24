from collections import deque

'''
bfs:
가까운 노드부터 탐색하는 너비 우선 탐색 알고리즘(dfs 는 최대한 멀리있는 노드 우선 탐색)

장점:
1) 현재 노드에서 가까운 곳부터 찾기 때문에 경로를 탐색 시 먼저 찾아지는 해답이 곧 최단경로임을 보장한다.
2) 노드의 수가 적고 깊이가 얕은 해가 존재할 때 효과적이다. 
'''


d = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs():
    global queue
    visited = [[0]*n for _ in range(n)]
    while queue:
        y, x = queue.popleft()
        for dx, dy in d:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < n and 0 <= rx < n:
                if miro[ry][rx] == 3:
                    return visited[y][x]
                if not miro[ry][rx] and visited[ry][rx] == 0:
                    visited[ry][rx] = visited[y][x] + 1
                    queue.append((ry, rx))
                    miro[ry][rx] = 1
                    continue

    return 0

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    queue = deque()
    miro = [list(map(int,input())) for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if miro[y][x] == 2:
                queue.append((y,x))
                miro[y][x] = 1
                break
    print(f'#{test_case} {bfs()}')




