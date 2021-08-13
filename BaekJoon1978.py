def sosu(n):
    if(n==1): return
    for i in range(2, n):
        if((n%i) == 0):
            return False
    return True

n = int(input())
num = list(map(int, input().split()))
cnt = 0

for i in range(len(num)):
    if(sosu(num[i])==True):
        cnt += 1

print(cnt)
