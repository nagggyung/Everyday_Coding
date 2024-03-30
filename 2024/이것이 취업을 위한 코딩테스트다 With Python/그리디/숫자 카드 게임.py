# n 이 1이될때까지
# n에서 1을 뺀다
# n을 k로 나눈다(k로 나누어 떨어질때 만)

# 풀이 방식 1
# - 행을 입력 받아올때 각 행에서 가장 작은 수를 뽑는다.
# - 행의 가장 작은 수들 중 가장 큰 수를 찾는다.

max_num = -10000
n, m = map(int, input().split())

for i in range(n):
    num = min(list(map(int, input().split())))
    max_num = max(max_num, num)

print(max_num)

