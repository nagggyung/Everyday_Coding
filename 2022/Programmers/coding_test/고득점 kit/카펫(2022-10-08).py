'''
규칙을 도출해 내기 엄청 쉬운 문제였는데
처음에 문제를 잘못이해해서 풀이하는 데 좀 오래 걸렸었다..

* 핵심
중앙에 위치하는게 노란색 카펫, 그 테두리가 갈색 카펫
따라서 문제 해결 조건은,
<조건>
1) 갈색 격자 수 + 노란색 격자 수 = Total 격자 수
2) 카펫의 가로 = 노란색가로 격자 수 -2 (테두리(갈색) 수 빼기)
3) 카펫의 세로 = 노란색세로 격자 수 -2 (테두리(갈색) 수 빼기)

'''

def solution(brown, yellow):
    answer = []
    total = brown+yellow
    
    for i in range(1, total):
        if total%i == 0:
            x = max(i, total//i)
            y = min(i, total//i)
            if (x-2)*(y-2) == yellow:
                answer.extend([x,y])
                break
            else:
                continue
                       

    return answer
            