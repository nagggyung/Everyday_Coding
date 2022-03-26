import collections

def solution(participant, completion):
    counter_parti = collections.Counter(participant)
    
    for name in completion:
        if counter_parti[name] == 1:
            del counter_parti[name]
        else:
            counter_parti[name] -= 1
    
    return list(counter_parti.keys())[0]