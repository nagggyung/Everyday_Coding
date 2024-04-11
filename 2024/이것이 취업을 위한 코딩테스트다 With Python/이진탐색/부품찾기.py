'''
매장에 부품이 n 개있다.
각 부품은 정수 형태의 고유한 번호가 있다.

m개 종류의 부품을 대량으로 구매하겠다며 견적서 요청했다
m개 종류를 전부 확인하여 견적서를 작성해야한다.
이때 가게 안에 부품이 모두 있는지를 확인하는 프로그램을 작성하자


'''

# binary search 로 풀어 보기
def binary_search(target):
    st, ed = 0, len(storage) -1

    while st <= ed:
        mid = (st + ed) // 2
        if storage[mid] == target:
            return True
        elif storage[mid] < target:
            st = mid+1
        else:
            ed = mid - 1
    return False



n = int(input())
storage = list(map(int, input().split()))

# storage 정렬. 이진 탐색을 이용 하기 위해서 사전에 정렬 수행
storage.sort()

m = int(input())
request_m = list(map(int, input().split()))

for num in request_m:
    if search(num):
        print('yes', end=' ')
    else:
        print('no', end=' ')

