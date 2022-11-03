# 예제 4-1 상하좌우

n = int(input())
commands = list(input().split())

command_map = {
              'L': [0,-1],
              'R': [0,1],
              'U': [-1,0],
              'D': [1,0] }
y,x = 1,1
for i in range(len(commands)):
  dy, dx = command_map[commands[i]]
  ry, rx = y+dy, x+dx

  if ry < 1 or ry > n or rx < 1 or rx > n:
    continue

  y,x = ry, rx 
print(y, x)
  
  