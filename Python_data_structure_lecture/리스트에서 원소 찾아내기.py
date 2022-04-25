def solution(L, x):
    answer = []

    # 해당 x 값이 리스트에 존재하지 않는 경우
    if x not in L:
        return [-1]

    start, end = 0, len(L)
    try:
        while True:
            loc = L[start:end].index(x)
            answer.append(loc+start)
            start = loc+start+1

    except:
        return answer
    