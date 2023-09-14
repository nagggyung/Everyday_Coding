# 1206. View
# 양 옆 두개씩 살펴 보기
'''
1206. View
양 옆 두개씩 살펴 보기

1) stand가 max value 여야 한다 -> left, right 리스트 둘다에서
2) max value 인 경우, stand 제외 두 번째 max value 값을 뺀다 -> left, right 각각 둘다 구함
3) 둘 중에 작은 값이 조망권 확보한 세대 이다.
'''

T = 10
for test_case in range(1, T + 1):
    n = int(input())
    buildings = list(map(int, input().split()))
    answer = 0

    for i in range(2, len(buildings)):
        stand = buildings[i]
        right = [buildings[i-1], buildings[i-2]]
        left = []
        if i+2 < len(buildings):
            left.append(buildings[i+2])
        if i+1 < len(buildings):
            left.append(buildings[i+1])

        # 검사 오른쪽
        check = True
        if right:
            temp1 = []
            temp1.extend(right)
            temp1.append(stand)
            if max(temp1) != stand:
                continue
        if left:
            temp2 = []
            temp2.extend(left)
            temp2.append(stand)
            if max(temp2) != stand:
                continue
        max_left = 0 if len(left)==0 else max(left)
        max_right = 0 if len(right)==0 else max(right)

        answer += min(stand-max_left, stand-max_right)

    print(f'#{test_case} {answer}')





