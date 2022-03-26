import collections

def solution(clothes):
    combi = collections.defaultdict(list)
    res = 1
    
    for item in clothes:
        combi[item[1]].append(item[0])
    
    for item in combi:
        # 부위별로 있는 옷의 개수에서 아무것도 안입는 경우 존재 +1
        res *= len(combi[item]) + 1
    
    # 모두 안입는 경우는 없으니 최종 값에서 -1    
    return res -1