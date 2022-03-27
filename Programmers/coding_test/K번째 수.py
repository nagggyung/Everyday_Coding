def solution(array, commands):
    res = []
    
    for command in commands:
        res.append(sorted(array[command[0]-1:command[1]])[command[2]-1])
    
    return res