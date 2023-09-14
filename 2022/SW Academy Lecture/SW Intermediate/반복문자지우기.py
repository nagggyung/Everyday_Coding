
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    words = input()
    result = []

    for w in words:
        if result and w == result[-1]:
            result.pop()
        else:
            result.append(w)
    print(f'#{test_case} {len(result)}')
