

def count_paper(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 3
    else:
        res = count_paper(num-1) + 2*count_paper(num-2)
    return res

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())//10
    print(f'#{test_case} {count_paper(N)}')
