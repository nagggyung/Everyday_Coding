def solution(L, x):
    for i in range(len(L)):
        if x <= L[i]:
            L.insert(i, x)
            return L
        
    # 주어진 리스트내에 존재하는 모든 원소들 보다 큰 정수가 주어지는 경우
    L.append(x)
    return L