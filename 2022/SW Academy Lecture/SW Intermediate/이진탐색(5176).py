def make_tree(n):
    # 1~ n+1 까지 순회 하면서 위치를 찾아 넣어준다.
    # binary_search_tree: left < 현재노드 <right
    # 현재노드 : index , left : index*2, right: index*2 +1
    # 중위 순회 구현으로 구현한다.
    global number
    if n < N + 1:
        make_tree(2 * n)
        tree[n] = number
        number += 1
        make_tree(2 * n + 1)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    number = 1

    make_tree(1)
    print(f'#{test_case} {tree[1]} {tree[N // 2]}')