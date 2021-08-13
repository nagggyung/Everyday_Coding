n = int(input())
num = list(map(int, input().split()))
cnt = 0
for i in range(len(num)):
    if(num[i]%10 == n):
        cnt += 1

print(cnt)