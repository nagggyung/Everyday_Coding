T = int(input())
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    num_list = list(map(int, input().split()))
    for _ in range(m):
        index, num = map(int, input().split())
        num_list.insert(index, num)

    print(f'#{test_case} {num_list[l]}')