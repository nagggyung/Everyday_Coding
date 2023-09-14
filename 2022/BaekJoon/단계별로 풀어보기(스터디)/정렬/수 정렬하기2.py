'''
시간 제한이 걸려 있어서,
input()을 사용할 경우 시간 초과가 될 수 있다.
따라서, sys.stdin.readline 을 이용하여 입력을 받는다.
'''



import sys
input=sys.stdin.readline

n=int(input())
num=[]

for i in range(n):
    num.append(int(input()))

for i in sorted(num):
    print(i)