from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    queue = deque(num_list)

    for i in range(M):
        num = queue.popleft()
        queue.append(num)

    print(f'#{test_case} {queue.popleft()}')

