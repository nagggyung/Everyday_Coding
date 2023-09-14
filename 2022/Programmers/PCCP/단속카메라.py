'''
그리디 알고리즘
탐욕 알고리즘이라고 말하는데, 말 그대로 선택의 순간마다 당장 눈앞에 보이는 최고의 상황만을 쫒아 최종적인 해답에 도달하는 방법이다.

'''
# 내풀이

def solution(routes):
    routes.sort(key=lambda x:x[1])
    cam = routes[0][1]
    count = 1
    for i in range(1, len(routes)):
        if cam >= routes[i][0] and cam <= routes[i][1]:
            continue
        else:
            cam = routes[i][1]
            count += 1
            
    return count

 