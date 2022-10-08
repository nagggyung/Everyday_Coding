def palindrome(n, m ,arr):
    # 전치행렬을 만들어서 가로탐색, 세로 탐색을 한번에 해결하자.
    # nxn 행렬이므로 가능 한 코드
    
    reversed_arr = list(zip(*arr))

    # 회문 탐색
    for i in range(n):
        for j in range(n-m+1):
            new_list1 = arr[i][j:j+m]
            new_list2 = reversed_arr[i][j:j+m]

            if new_list1 == new_list1[::-1]:
                return "".join(new_list1)
            if new_list2 == new_list2[::-1]:
                return "".join(new_list2)



Test_case = int(input())
for t in range(1, Test_case + 1):
    n, m = map(int, input().split())
    str_array = [list(input()) for _ in range(n)]

    print(f'#{t} {palindrome(n,m,str_array)}')


