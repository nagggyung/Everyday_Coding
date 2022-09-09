from collections import defaultdict

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    card_list = input()
    int_dict = defaultdict(int)

    for card_num in card_list:
        int_dict[card_num] += 1

    max_count = max(int_dict.values())
    num = [k for k, v in int_dict.items() if v == max_count]
    print(f'#{test_case} {max(num)} {max_count}')
