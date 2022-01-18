def sosu(n):
    if(n==1): return
    for i in range(2, n):
        if((n%i) == 0):
            return False
    return True

m = int(input())
n = int(input())
sum = 0
minNum = n

for i in range(m, n+1):
    if(sosu(i)==True):
        sum += i
        if(minNum > i):
            minNum = i

if(sum==0):
    print(-1)
else:
    print(sum)
    print(minNum)
