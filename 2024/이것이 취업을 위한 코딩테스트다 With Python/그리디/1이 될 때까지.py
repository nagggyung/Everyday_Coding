# n 이 1이될때까지
# n에서 1을 뺀다
# n을 k로 나눈다(k로 나누어 떨어질때 만)

# 풀이 방식 1
def question1(n, k):
    count = 0

    while n > 1:
        if (n % k) == 0:
            n = n//k
        else:
            n -= 1
        count += 1

    print(count)




n, k = map(int, input().split())
question1(n, k)

