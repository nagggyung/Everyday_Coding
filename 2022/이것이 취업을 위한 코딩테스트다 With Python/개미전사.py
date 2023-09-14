# 개미 전사
# DP 문제 푸는 법 --> 점화식을 알아내는 법

# ai = max(ai-1, ai-2 + k(ai식량))

n = int(input())
store = list(map(int, input().split()))
dp = [0]*(n+1)
dp[0] = store[0]
dp[1] = store[1]

for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2]+store[i])

print(dp[n-1])