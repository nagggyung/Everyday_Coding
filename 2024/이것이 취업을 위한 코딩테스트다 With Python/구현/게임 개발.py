'''
게임개발
n * m 크기의 게임 장. 각각의 칸은 육지 또는 바다
맵의 각 칸은 (A, B) 로 나타낼 수 있고 A는 북쪽으로부터 떨어진 칸의 개수
B는 서쪽으로 부터 떨어진 칸의 개수이다.

* 캐릭터는 상하 좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.

* 매뉴얼
1) 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)
부터 차례대로 갈 곳을 정한다.
2) 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전한다음
왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만하고
1단계로 돌아간다.
3) 만약 네 방향 모두 이미 가본 칸이거나, 바다로 되어 있는 칸인 경우에는, 바라보는 방향을
유지한채로 한 칸 뒤로가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로
갈 수 없는 경우에는 움직임을 멈춘다.

* 매뉴얼에 따라 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트
캐릭터가 방문한 칸의 수를 출력하는 프로그램 만들기

'''

# 회전 방향
def turn_left(direction):
    rule = [0, 3, 2, 1] # 반시계 방향 회전
    idx = (rule.index(direction) + 1) % len(rule)

    return rule[idx]

# 이동 방향
def move(direction):
    if direction == 0:
        return [-1, 0]
    elif direction == 3:
        return [0, -1]
    elif direction == 2:
        return [-1, 0]
    else:
        return [0, 1]


def game(y, x, direction):
    global count
    global game_map
    game_map[y][x] = 1
    turn_count = 0

    while True:
        # turn_left
        direction = turn_left(direction)

        # move
        dy, dx = move(direction)
        ry, rx = y+dy, x+dx

        # 가보지 않은 칸이 존재
        if game_map[ry][rx] == 0:
            y, x = ry, rx
            count += 1
            game_map[ry][rx] = 1

            continue
        else:

            # 네 방향 모두 돌았음
            if turn_count == 4:
                dy, dx = move(direction)
                ry, rx = y-dy, x-dx

                if game_map[ry][rx] == 1:
                    break
                else:
                    y, x = ry, rx
                    count += 1
                    turn_count = 0
                    continue

            turn_count += 1




n, m = map(int, input().split())
y, x, direction = map(int, input().split())
count = 1  # 무조건 시작 칸은 방문 하니까!
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

game(y, x, direction)
print(count)

# game_map: 1 -> 바다, 0 -> 육지
# 방문한 영역은 1로 바꾸면 됨.


