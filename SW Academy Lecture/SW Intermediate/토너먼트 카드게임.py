# 5일차 - 토너먼트 카드게임


def div_group(st, ed):
    if st == ed:
        return st
    else:
        left = div_group(st, (st+ed)//2)
        right = div_group((st+ed)//2 + 1, ed)
        winner = game(left, right)
        return winner

def game(left, right):
    if card_list[left-1] == card_list[right-1]:
        return left
    elif card_list[left-1] == 1: #가위
        if card_list[right-1] == 2:
            return right
        else:
            return left
    elif card_list[left-1] == 2: # 바위
        if card_list[right-1] == 3:
            return right
        else:
            return left
    else: # 보
        if card_list[right-1] == 1:
            return right
        else:
            return left

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    card_list = list(map(int, input().split()))

    print(f'#{test_case} {div_group(1, n)}')
