from collections import defaultdict

def solution(genres, plays):
    hash_map = defaultdict(list)
    hash_count = defaultdict(int)
    answer = []
    for i, data in enumerate(genres):
        hash_map[data].append([i, plays[i]])
        hash_count[data]+=plays[i]
  # sort는 리스트만 정렬 가능 --> 반환 리스트 형태
  # sorted iterable 정렬 가능 --> 반환 리스트 형태
    hash_count = dict(sorted(hash_count.items(), key=lambda x:-x[1]))
    for key in hash_count:
        temp = sorted(hash_map[key], key=lambda x:(x[1], -x[0]))
        for _ in range(2):
            if temp:
                answer.append(temp.pop()[0])
    return answer

'''
# 다른 사람의 풀이..

def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

'''