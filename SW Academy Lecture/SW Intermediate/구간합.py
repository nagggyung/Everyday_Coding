T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    num_list = list(map(int, input().split()))
    st = 0
    res_list = []

    while st+m<n+1:
        res_list.append(sum(num_list[st:st+m]))
        st += 1
    print(f'#{test_case} {max(res_list)-min(res_list)}')