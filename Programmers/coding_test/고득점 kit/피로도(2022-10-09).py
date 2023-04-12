'''
순열: permutations -- 순서 고려 (a,b) != (b,a)
조합: combinations -- 순서 고려 x (a,b) == (b,a)

'''


from itertools import permutations

def solution(k, dungeons):
    cases = permutations(dungeons, len(dungeons))
    res = []
    
    for case in cases:
        energy = k
        count = 0
        for piro, drain in case:
            if energy >= piro:
                energy -= drain
                count += 1
        res.append(count)

    return max(res)

'''
# 다른사람의 풀이
- dfs 이용

answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
'''