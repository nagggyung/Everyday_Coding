# 델타 탐색:
# 2차 배열의 한 좌표에서 4방향(혹은 8방향 등 필요 요소)의 인접 배열 요소를 탐색하는 방법
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def find_way():
    while stack:
        y, x = stack.pop()
        graph[y][x] = 1

        for dx, dy in delta:
            ry = y+dy
            rx = x+dx

            if 0 <= ry < n and 0 <= rx < n:
                if graph[ry][rx] == 3:
                    return 1
                if not graph[ry][rx]:
                    stack.append((ry, rx))
                    continue
    return 0


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    stack = []
    # 미로 생성
    graph = [list(map(int, input())) for _ in range(n)]

    # 시작 점 찾기
    for y in range(n):
        for x in range(n):
            if graph[y][x] == 2:
                stack.append((y, x))
                break

    print(f'#{test_case} {find_way()}')


