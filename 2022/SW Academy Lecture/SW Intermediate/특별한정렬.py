T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    not_sorted = list(map(int, input().split()))
    res_list = []

    for _ in range(len(not_sorted)):
        if len(not_sorted) == 0:
            break
        if len(res_list) == 10:
            break
        res_list.append(str(max(not_sorted)))
        res_list.append(str(min(not_sorted)))

        not_sorted.remove(max(not_sorted))
        not_sorted.remove(min(not_sorted))

    res_str = ' '.join(res_list)
    print(f'#{test_case} {res_str}')



