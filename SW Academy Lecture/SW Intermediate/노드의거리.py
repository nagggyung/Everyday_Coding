# bfs 문제 푸는 방법 익히기

from collections import deque

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        start_node = queue.popleft()
        for node in range(1, v+1):
            if graph[start_node][node] and not visited[node]:
                queue.append(node)
                visited[node] = 1
                distance[node] = distance[start_node] + 1
                if node == end_node:
                    return distance[node]
    return 0
T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[0 for _ in range(v+1)] for _ in range(v+1)]
    visited = [0] * (v+1)
    distance = [0] * (v+1)

    for _ in range(e):
        start, end = map(int, input().split())
        graph[start][end] = 1
        graph[end][start] = 1

    start_node, end_node = map(int, input().split())

    print(f'#{test_case} {bfs(start_node)}')
