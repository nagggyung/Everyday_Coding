'''
조건을 다 찾아서 구현했지만,
문제에 대한 이해가 부족해서 잘못구현하느라
시간을 많이 썼던 문제이다.

Linked list 를 이용해서 구현하는 문제 파트인데..
Linked List 는 어떻게 활용해서 풀어햐 할까..?

'''

T = int(input())
for test_case in range(1, T + 1):
    n,m,k = map(int, input().split())
    num_list = list(map(int, input().split()))
    st = 0

    for _ in range(k):
        st = st + m
        if st > len(num_list):
            st -= len(num_list)
        if not st:
            num_list.insert(0, num_list[-1]+num_list[0])
        elif st == len(num_list):
            num_list.append(num_list[-1] + num_list[0])
        else:
            num_list.insert(st, num_list[st-1] + num_list[st])

    res = []
    for item in num_list[::-1]:
        if len(res)==10:
            break
        res.append(str(item))
    print(f'#{test_case} {" ".join(res)}')

