T = int(input())
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree_list = [0 for _ in range(n+1)]
    for _ in range(m):
        index, data = map(int, input().split())
        tree_list[index] = data
    for i in range(n, 0, -1): # n~1 까지 -1 씩 감소하며 반복
        if not tree_list[i]:
            if i*2+1 > n:
                tree_list[i] = tree_list[i*2]
                continue
            tree_list[i] = tree_list[i*2] + tree_list[i*2 + 1]
        else:
            continue
    print(f'#{test_case} {tree_list[l]}')
