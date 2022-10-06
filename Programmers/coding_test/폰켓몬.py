from collections import defaultdict

def solution(nums):
    hash_map = defaultdict(int)
    category_num = len(nums)//2
    for num in nums:
        hash_map[num] += 1

    # 종류 수 최댓 값
    res = []
    while len(res) < category_num:
        for key in hash_map.keys():
            if len(res) == category_num:
                break
            if hash_map[key]:
                hash_map[key] -=1
                res.append(key)
            else:
                continue
    res_dict = defaultdict(int)
    for item in res:
        res_dict[item] += 1

    answer = len(list(res_dict.keys()))
    return answer


'''
# 다른 사람 풀이..

def solution(ls):
    return min(len(ls)/2, len(set(ls)))
    
- min()으로 해결이 가능 한 문제였다.. 
'''