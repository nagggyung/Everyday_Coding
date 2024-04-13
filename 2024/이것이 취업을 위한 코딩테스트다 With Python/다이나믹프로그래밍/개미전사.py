'''
# 개미전사

개미 전사는 부족한 식량 충당하고자 메뚜기 마을의 식량창고를 공격.
식량 창고는 일직선으로 이어져 있다.
각 식량창고에는 정해진 수의 식량을 저장하고 있으며, 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정이다.

이때, 정찰병들은 일직선상에 존재하는 식량창고중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.
들키지 않기위해 최소한 한 칸 이상 떨어진 식량차고를 약탈해야한다.

[1, 3, 1, 5]

3, 5 = 8 최댓값
식량의 최댓 값을 구하라.

'''

n = int(input())
storage = list(map(int, input().split()))

# 0, 1, 2, 3

dp = [0]*(n)
# dp[i] = max(dp[i-1], dp[i-2] + k(i))

# 다이나믹 프로그래밍 (보텀업)
dp[0] = storage[0]
dp[1] = max(storage[0], storage[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + storage[i])

# 결과
print(dp[n-1])