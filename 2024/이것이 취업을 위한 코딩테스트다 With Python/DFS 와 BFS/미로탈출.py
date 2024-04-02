'''

# 미로탈출
(1,1): 현재위치 - (n,m):출구
한번에 한칸 씩 이동가능
괴물은 0 위치에 있음
괴물이 없는 부분은 1

탈출을 위한 최소 칸의 위치
시작 칸과 마지막 칸을 모두 포함해서 계산

bfs -> deque
# 최소거리 문제 풀이 시에 칸 별로 시작 점에서 몇칸 이동했는지를 더해주면
시작 위치부터 도착 위치 까지의 최소 이동 거리를 확인할 수 있다(즉, 몇칸이동했는지를 알 수 있다)

'''

from collections import deque


def bfs(x, y):
    queue.append([x, y])
    global count

    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            rx, ry = x+dx, y+dy

            if rx < 0 or rx > n-1 or ry < 0 or ry > m-1:
                continue

            if miro[rx][ry] == 0:
                continue

            if miro[rx][ry] == 1:
                # 몇 칸 이동을 했는지 표시
                miro[rx][ry] = miro[x][y] + 1

                queue.append([rx, ry])
                continue
    print(miro)
    return miro[n-1][m-1]


queue = deque()

n, m = map(int, input().split())
miro = []
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


for _ in range(n):
    miro.append(list(map(int, input())))

print(bfs(0, 0))


