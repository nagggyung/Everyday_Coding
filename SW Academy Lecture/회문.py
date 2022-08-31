

def palindrome(N,M,arr):
  res = []
  # 가로 회문 탐색
  for i in range(N):
    for j in range(N-M+1):
      new_list = arr[i][j:j+M]
      if new_list == new_list[::-1]:
        res.append(new_list)
        return res

  # 세로 회문 탐색
  for i in range(N):
    for j in range(N-M+1):
      new_list = []
      for k in range(M):
        new_list.append(arr[j+k][i])
        if new_list == new_list[::-1]:
          res.append("".join(new_list))
          return res

Test_case = int(input())
for t in range(1, Test_case + 1):
  N, M = map(int, input().split())
  # n x n arr
  arr = []
  for i in range(N):
    arr.append(input())


  print(f'#{t} {palindrome(N,M,arr)[0]}')