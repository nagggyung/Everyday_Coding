'''
효율적인 화폐 구성

dp 문제..다시 이해해보기!
'''
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
dp = [10001]*m

for i in range(n):
    for j in range(arr[i], m+1):
        if dp[j-arr[i]] != 10001:
            dp[j] = min(dp[j], dp[j-arr[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
        
