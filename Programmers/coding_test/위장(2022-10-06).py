'''
모자) a,b,c 가 있는 경우
모자를 안쓰는 경우, a, b, c 총 3가지가 있으므로 각 item 갯수에 +1 을 해준다.(각 item의 경우의 수)

각 item의 경우의 수를 곱해준다. 

다 벗는 경우는 없으므로 최종 답에 -1 을 해준다.
'''


from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)
    for item, clothes_type in clothes:
        clothes_dict[clothes_type].append(item)
    answer = 1
    
    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key]) + 1
    
    return answer-1

    
    '''
    # 다른 사람의 풀이
    
    import collections
    from functools import reduce

    def solution(c):
        return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
    '''