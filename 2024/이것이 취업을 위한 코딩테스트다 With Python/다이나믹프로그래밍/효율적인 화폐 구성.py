'''
# 효율적인 화폐 구성

n 가지 종류의 화폐가 있다.
화폐의 개수를 최소한으로 이용하여 그 가치의 합이 m원이 되도록 하기

불가능 할 때는 -1을 출력한다.

'''

n, m = map(int, input().split())
value = []

for _ in range(n):
    value.append(int(input()))
value.sort()

# 최댓값이 10000 이므로 값이 존재하지 않는 경우로 10001 로 초기화 한다.

# 한번 계산 된 결과를 저장하기 위한 dp 테이블
d = [10001] * (m+1)

# 화폐를 하나도 사용하지 않았을 때 만들 수 있다.
d[0] = 0 

# 다이나믹 프로그래밍 진행(보텀업)
for v in value:
    for j in range(v, m+1):
        if d[j-v] != 10001: # i-k 원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-v]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])








