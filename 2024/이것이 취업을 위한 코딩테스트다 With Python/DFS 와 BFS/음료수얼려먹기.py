'''
n*m 크기의 얼음 틀이 있다.
뚫려있는 부분은 0, 칸막이가 있는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상,하,좌,우 로 붙어있는 경우 서로 연결된것으로 강주한다.
얼음틀모양이 주어졌을 때 생성되는 총 아이스크림 개수를 구하는 프로그램

dfs
- 재귀 함수(스택)

'''



def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False

    if ice_map[x][y] == 0:
        ice_map[x][y] = 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True

ice_map = []
n, m = map(int, input().split())
for _ in range(n):
    ice_map.append(list(map(int, input())))

count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1


print(count)

