'''
heapify와 heappush 결과가 다를 수 있다는 점을
몰랐어서 잘못 된 풀이로 시간이 꽤 걸렸던 문제이다..

heapify는 리스트를 heap 구조로 바꿀 때 사용하는 함수인데
최소 값을 반환 하는데는 문제 없지만 heap 구조로 바꾼 상태에서 데이터를 가져와야하는 상황에서는
적합하지 않을 수 있다. 

heappush를 한 경우와 결과 값이 다를 수 있다.

'''



T = int(input())

import heapq
for test_case in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    heap_list = []
    sum_nums = 0
    
    for item in num_list:
        heapq.heappush(heap_list, item)
    heap_list = [0]+heap_list


    while n > 0:
        # 이진트리 부모 인덱스 = (자식노드 인덱스)//2
        n = n//2
        sum_nums += heap_list[n]

    print(f'#{test_case} {sum_nums}')