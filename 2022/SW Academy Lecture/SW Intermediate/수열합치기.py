T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    # m개의 수열
    num_list = [list(map(int,input().split())) for _ in range(m)]
    new_list = num_list[0]

    for i in range(1, m):
        for index, data in enumerate(new_list):
            if data > num_list[i][0]:
                # 특정 위치에 삽입 시, 리스트의 슬라이싱을 이용할 수 있다.
                new_list[index:index] = num_list[i]
                break
            if index == len(new_list)-1:
                new_list = new_list + num_list[i]
                break
    res = []
    for item in new_list[::-1]:
        if len(res) == 10:
            break
        res.append(str(item))

    print(f'#{test_case} {" ".join(res)}')

