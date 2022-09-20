from itertools import combinations
# itertools 라이브러리의 combinations 메서드 사용하면 하나의 리스트에서 모든 부분집합 리스트를 얻을 수 있다.
# combinations(list, 부분집합의 수)



T = int(input())
for test_case in range(1, T + 1):
    num_list = [i for i in range(1,13)]
    n, k = map(int, input().split())
    partitions = combinations(num_list, n)
    k_count = 0
    for parti in partitions:
        if sum(parti) == k:
            k_count +=1

    print(f'#{test_case} {k_count}')
