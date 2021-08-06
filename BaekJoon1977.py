M = int(input())
N = int(input())
i = 1
res =[]
sum = 0
while(i**2 <= N):
    if(i**2 >= M and i**2 <= N):
        res.append(i**2)
        sum += i**2
    i += 1

if res == []:
    print(-1)
else:
    print(sum)
    print(min(res))
