from collections import defaultdict

def count_nodes(n):
    global count

    if len(tree_map[n]) == 0:
        return
    for item in tree_map[n]:
        count_nodes(item)
        count += len(tree_map[item])

T = int(input())
for test_case in range(1, T + 1):
    e, n = map(int, input().split())
    tree = list(map(int, input().split()))
    tree_map = defaultdict(list)


    for i in range(0, len(tree)-1, 2):
        tree_map[tree[i]].append(tree[i+1])
        
    # count 변수를 n과 n 자식 노드 수의 합으로 초기화 해준다.
    count = len(tree_map[n]) + 1
    count_nodes(n)

    print(f'#{test_case} {count}')