n, k = map(int, input().split())
num = []
for i in range(1,n+1):
    if n%i ==0:
        a = n//i
        num.append(a)

num.sort()
if(len(num)<k):
    print(0)
else:
    print(num[k-1])