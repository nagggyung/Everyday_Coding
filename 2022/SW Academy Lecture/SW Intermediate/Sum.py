# 1209. sum

T = 10
for test_case in range(1, T + 1):
    test_num = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []
    arr_col = list(zip(*arr))

    # 행, 열의 합
    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr_col[i][j]
        sum_list.append(sum_row)
        sum_list.append(sum_col)


    # 대각선
    s_1, s_2 = 0, 0
    for i in range(100):
        for j in range(100):
            if i == j:
                s_1 += arr[i][j]
            if 100-i-1 == j:
                s_2 += arr[i][j]

    sum_list.append(s_1)
    sum_list.append(s_2)

    print(f'#{test_case} {max(sum_list)}')













