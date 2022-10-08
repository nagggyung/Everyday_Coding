from collections import defaultdict

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    count_dict = defaultdict(int)
    for s in str1:
        count_dict[s] = str2.count(s)

    print(f'#{test_case} {max(count_dict.values())}')