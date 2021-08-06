n = int(input())

while(n):
    p = int(input())
    max = 0
    mName = ""
    for i in range(p):
       num, name = input().split(" ")
       num = int(num)
       if num > max:
           max = num
           mName = name
    print(mName)
    n -= 1

