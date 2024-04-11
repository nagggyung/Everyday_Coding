'''
# 떡볶이 떡 만들기
절단기에 높이 h를 지정하면 줄지어진 떡을 한번에 절단한다
높이가 h보다 긴 떡은 h위의 부분이 잘릴 거고, 낮은 떡은 잘리지 않는다

손님이 왔을때 요청한 총 길이가 m일때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하라

이진탐색 문제
'''



n, m = map(int, input().split())
arr = list(map(int, input().split()))

# arr : 0~ max(arr)

st, ed = 0, max(arr)
result = 0

while st <= ed:
    total = 0
    h = (st + ed) // 2
    for t in arr:
        if t > h:
            total += (t-h)

    if total < m:
        ed = h - 1
    else:
        result = h
        st = h + 1


print(result)


