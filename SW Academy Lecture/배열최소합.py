def find_min_sum(y, sum):
    # 값을 할당하기 위해서는 global 선언을 해야한다.
    global min_sum
    if y == n:
        if sum < min_sum:
            min_sum = sum
        return
    # 가지치기
    if sum >= min_sum:
        return
    for i in range(n):
        # 갔던 세로줄은 사용 불가하게 바꾸기
        if visited[i]:
            visited[i] = False
            find_min_sum(y+1, sum+arr[y][i])
            visited[i] = True

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [True for _ in range(n)]

    min_sum = 987654321
    find_min_sum(0,0)
    print(f'#{test_case} {min_sum}')
