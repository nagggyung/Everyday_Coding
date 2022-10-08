# 정답 풀이..
# dfs 개념이 많이 부족하다! 정리하자..! 


def dfs(start, end):
    stack = []
    visited = [False]*(v+1)
    stack.append(start)

    while stack:
        start = stack.pop()
        visited[start] = True

        for i in range(1, v+1):
            if not visited[i] and graph[start][i]:
                stack.append(i)

    if visited[end]:
        return 1
    else:
        return 0


T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[0 for _ in range(v+1)] for _ in range(v+1)]

    for _ in range(e):
        start, end = map(int, input().split())
        graph[start][end] = 1

    start, end = map(int, input().split())
    print(f'#{test_case} {dfs(start, end)}')