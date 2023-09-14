T = int(input())
for test_case in range(1, T + 1):
    # n: 수열의 길이, m: 추가 횟수, l: 출력할 인덱스 번호
    n,m,l = map(int, input().split())
    num_list = list(map(int,input().split()))

    # I : Insert
    # D : Delete
    # C : replace

    for _ in range(m):
        # connad, index, num
        command = list(input().split())
        if 'I' in command:
            num_list.insert(int(command[1]), command[2])
            continue
        if 'D' in command:
            del num_list[int(command[1])]
            continue
        if 'C' in command:
            num_list[int(command[1])] = command[2]
            continue
    if l < len(num_list):
        print(f'#{test_case} {int(num_list[l])}')
    else:
        print(f'#{test_case} {-1}')

