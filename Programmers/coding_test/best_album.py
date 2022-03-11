def solution(genres, plays):
    hash_map = {}
    answer = []
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in hash_map:
            hash_map[genre] = {
                'play' : { 
                    i : play
                },
                'total_play' : play
            }
        else:
            hash_map[genre]['play'][i] = play
            hash_map[genre]['total_play'] += play

    #print(hash_map.items())
    # total_play 값으로 정렬
    temp = sorted(hash_map.items(), key = lambda x : -x[1]['total_play'])
    
    # play값 정렬
    for item in temp:
        target = item[1]['play']
        # print(target)
        item[1]['play'] = sorted(target.items(), key = lambda x:(-x[1], x[0]))
    
    temp = dict(temp)
    
    for key in temp:
        try:
            answer += [temp[key]['play'][0][0], temp[key]['play'][1][0]]
        except:
            answer +=  [temp[key]['play'][0][0]]
    
    return answer