def solution(routes):
    routes.sort(key=lambda x:x[1])
    cam = routes[0][1]
    count = 1
    for i in range(1, len(routes)):
        if cam >= routes[i][0] and cam <= routes[i][1]:
            continue
        else:
            cam = routes[i][1]
            count += 1
            
    return count