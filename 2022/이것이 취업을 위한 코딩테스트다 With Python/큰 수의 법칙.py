n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

max_num = max(num_list)
smax_num = max(num_list[:len(num_list)-1])

total = 0
count = 0
m_count = 0

while(m_count<m):
  count += 1
  m_count += 1
  if count <= k:
    total += max_num
  else:
    total += smax_num
    count = 0

print(total)   

  