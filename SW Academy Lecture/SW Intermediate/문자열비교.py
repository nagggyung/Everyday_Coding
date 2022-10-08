T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    # 파이썬에서 특정 문자열 포함여부 확인 시
    # in, not in 키워드를 이용하여 확인할 수 있다.
    # in 키워드를 사용하는 경우, 결과 값이 존재하면 True, 존재하지 않은 경우 False 값을 리턴하게 된다.
    
    if str1 in str2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')



