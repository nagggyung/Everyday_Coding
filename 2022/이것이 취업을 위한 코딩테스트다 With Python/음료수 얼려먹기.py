# 이것이 코딩테스트다 chap5 dfs/bfs 
# connected block count
# 블로그 정리

def dfs(y, x):
    if y>n-1 or y<0 or x>m-1 or x<0:
        return False

    if graph[y][x] == 0:
        graph[y][x] = 1 # 방문처리

        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)

        return True
    return False



n, m = map(int, input().split()) # n: 세로, m: 가로
graph= []
for _ in range(n):
    graph.append(list(map(int, input())))
answer = 0
for i in range(n):
    for j in range(m):
        # 현재위치에서 dfs 수행
        if dfs(i,j) ==True:
            answer += 1

print(answer)




