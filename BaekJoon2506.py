n = int(input())
scores = list(map(int, input().split()))
total = []
if(scores[0]==1):
    total.append(1)
else:
    total.append(0)
for i in range(1, len(scores)):
    if(scores[i] == 0):
        total.append(0)
    if(scores[i]>0):
        if(scores[i-1]>0):
            total.append(total[i-1]+1)
        else:
            total.append(1)

print(sum(total))