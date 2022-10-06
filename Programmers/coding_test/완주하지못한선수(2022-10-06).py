from collections import defaultdict
def solution(participant, completion):
    answer = ''
    parti_dict = defaultdict(int)
    for person in participant:
        parti_dict[person] += 1
    
    for name in completion:
        if name in parti_dict:
            parti_dict[name] -= 1
    
    for key, value in parti_dict.items():
        if value:
            answer = key
    
    return answer
        
'''
# 다른 사람 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
'''