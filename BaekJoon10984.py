T = int(input())

for i in range(T):
    totalC = 0
    totalG = 0
    N = int(input())
    for j in range(N):
        c, g = map(float, input().split(" "))
        totalC += c
        totalG += c*g

    print("%d"%totalC +" " + "%.1f"%(totalG/totalC))