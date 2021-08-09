from math import gcd

def lcm(a,b):
    return (a*b)/gcd(a,b)

num1, num2 = map(int, input().split(" "))

print(gcd(num1,num2))
print(int(lcm(num1, num2)))