T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    arr = list(map(int, input().split()))

    for _ in range(dump):
        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))

        arr[max_idx] -= 1
        arr[min_idx] += 1

    print(f'#{test_case} {max(arr)-min(arr)}')