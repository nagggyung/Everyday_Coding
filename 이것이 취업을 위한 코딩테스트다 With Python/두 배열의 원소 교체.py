n, k = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

for _ in range(k):
  aidx = arr_A.index(min(arr_A))
  bidx = arr_B.index(max(arr_B))

  arr_A[aidx], arr_B[bidx] = arr_B[bidx], arr_A[aidx]

print(sum(arr_A))