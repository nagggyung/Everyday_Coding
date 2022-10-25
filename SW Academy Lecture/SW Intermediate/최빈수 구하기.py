# 1204. 최빈수 구하기

from collections import Counter

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    counter_list = Counter(list(map(int, input().split())))
    max_v = max(counter_list.values())

    for k, v in counter_list.items():
        if v == max_v:
            print(f'#{test_case} {k}')
            break


