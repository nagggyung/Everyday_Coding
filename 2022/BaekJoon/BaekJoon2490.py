for i in range(3):
    sum = 0
    game = list(map(int, input().split()))
    for j in range(len(game)):
        sum += game[j]
    if sum == 3:
        print("A")
    elif sum == 2:
        print("B")
    elif sum == 1:
        print("C")
    elif sum == 0:
        print("D")
    else:
        print("E")
