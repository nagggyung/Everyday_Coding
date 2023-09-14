def solution(L, x):

    
    low_idx, upper_idx = 0, len(L)-1
    idx = -1
    
    while low_idx <= upper_idx:
        middle_idx = (low_idx + upper_idx)//2
        if L[middle_idx] == x:
            return middle_idx
        elif L[middle_idx] < x:
            low_idx = middle_idx + 1
        else:
            upper_idx = middle_idx - 1
    
    # 리스트 L에 x값 존재하지 않는 경우 -1 리턴
    return -1

        