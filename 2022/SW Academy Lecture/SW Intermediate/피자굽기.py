from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    c = deque()
    queue = deque()
    res = 0
    for i, v in enumerate(pizza):
        c.append([i+1,v])
    queue.append(c.popleft())

    while queue:
       # 화덕에 피자 넣기
       if len(queue) < n and c:
           queue.append(c.popleft())
           continue

       res = queue[0]
       l, cheese = queue.popleft()
       l, cheese = l, cheese//2

       # cheese 가 0
       if not cheese:
           continue
       else:
           queue.append([l, cheese])

    print(f'#{test_case} {res[0]}')
