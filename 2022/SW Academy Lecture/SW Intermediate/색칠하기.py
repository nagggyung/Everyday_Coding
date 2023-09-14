T = int(input())
for test_case in range(1, T + 1):
    matrix = [[0]*10 for _ in range(10)]
    n = int(input())
    color_matrix = [list(map(int, input().split())) for _ in range(n) ]

    st = 0
    purple_count = 0

    while st < len(color_matrix):
        y1,x1,y2,x2,color = color_matrix[st]
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                matrix[y][x] += color
                if matrix[y][x] == 3:
                    purple_count += 1

        st+=1

    print(f'#{test_case} {purple_count}')

