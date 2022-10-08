# 재귀로 풀면 recursive 에러 지옥에 빠짐

def binary_search(p, target, steps):
    l = 1
    r = p

    while l <= r:
        mid = (l+r)//2
        if mid == target:
            return steps
        elif target < mid:
            r = mid
            steps += 1
        else:
            l = mid
            steps += 1



T = int(input())


for test_case in range(1, T + 1):
    p, a, b = map(int, input().split())

    a_search = binary_search(p,a,1)
    b_search = binary_search(p,b,1)

    if a_search > b_search:
        print(f'#{test_case} B')
    elif a_search < b_search:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')







