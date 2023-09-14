# 예제 4-2 시각

n = int(input())

count = 0

for hour in range(0, n+1):
  for min in range(0, 60):
    for sec in range(0,60):
      temp = str(hour)+str(min)+str(sec)
      if hour == n and min == 59 and sec == 59:
        break
      if '3' in temp:
        count+=1

print(count)
