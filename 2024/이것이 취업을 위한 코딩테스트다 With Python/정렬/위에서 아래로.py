'''
# 위에서 아래로

큰 수부터 작은수로 정렬
수열을 내림차순으로 정렬

공백으로 구분하여 출력

'''


n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(len(arr)):
    print(arr[i], end = ' ')