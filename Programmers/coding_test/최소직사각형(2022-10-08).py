def solution(sizes):
    w_list = []
    h_list = []
    
    for w,h in sizes:
        if w>h:
            w_list.append(w)
            h_list.append(h)
        else:
            w_list.append(h)
            h_list.append(w)
    return max(w_list)*max(h_list)

    '''
    #다른 사람 풀이
    def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
    '''