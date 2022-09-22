# dp 이용 문제 풀이

def paper_num(n):
    global memo

    if n == 1:
        return memo[0]
    elif n == 2:
        return memo[1]
    elif n>2 and len(memo) < n:
        memo.append(paper_num(n-1) + 2*paper_num(n-2))
    return memo[n-1]

T = int(input())
for test_case in range(1, T + 1):
    memo = [1,3]
    n = int(input())
    print(f'#{test_case} {paper_num(n//10)}')
