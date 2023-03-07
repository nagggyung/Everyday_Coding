from collections import defaultdict

def solution(id_list, report, k):
    # 중복신고제거
    report = list(set(report))
    answer = []
    
    repo_cnt = defaultdict(int)
    ids = defaultdict(set)
    
    for id in report:
        user, repo_user = id.split()
        repo_cnt[repo_user] += 1
        ids[user].add(repo_user)
    
    for id in id_list:
        res = 0
        for v in ids[id]:
            if repo_cnt[v] >= k:
                res += 1
        answer.append(res)
    return answer
                
            