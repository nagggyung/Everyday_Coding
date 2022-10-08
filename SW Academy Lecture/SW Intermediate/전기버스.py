T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    '''
    K : 한 번 충전으로 최대 이동 횟수
    N : 종점
    M : 충전기 설치된 정류장 수
    '''
    k, n, m = map(int, input().split())
    gas_stations = list(map(int, input().split()))
    bus_stations = [0 for _ in range(n+1)]

    for i in gas_stations:
        bus_stations[i] = 1

    # bus_stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    cnt = 0
    curr_loc = 0
    k_loc = curr_loc + k

    while k_loc < n:
        if k_loc == curr_loc:
            cnt = 0
            break
        if bus_stations[k_loc] == 1:
            cnt += 1
            curr_loc = k_loc
            k_loc = curr_loc + k
            continue
        if not bus_stations[k_loc]:
            k_loc -= 1
            continue
            
    print(f'#{test_case} {cnt}')

