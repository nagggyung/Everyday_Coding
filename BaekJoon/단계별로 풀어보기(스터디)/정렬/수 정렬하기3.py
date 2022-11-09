'''
메모리 초과 문제 발생.

input() 으로 입력을 받으면 메모리 초과가 날 수 있다.
sys 를 사용하여 입력을 받아주고, 배열을 생성해준다.
배열에는 각 숫자의 개수가 들어가게 된다.

'''

# 10989번

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

