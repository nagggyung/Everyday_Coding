T = int(input())

for i in range(T):
    price = int(input())
    op = int(input())
    total = 0
    optTotal = 0
    for j in range(op):
        optN, optPrice = map(int, input().split(" "))
        optTotal += (optN * optPrice)
    total = price + optTotal
    print(total)
