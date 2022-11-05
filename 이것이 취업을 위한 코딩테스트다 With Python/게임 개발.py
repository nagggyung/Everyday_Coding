# 회전 방향
def turn_left(direction):
  rule = [0,3,2,1] 
  idx = (rule.index(direction)+1)%len(rule)
  return rule[idx]

# 이동 방향
def move_block(direction):
  if direction == 0:
    return [-1,0]
  elif direction == 3:
    return [0,-1]
  elif direction == 2:
    return [1,0]
  else: 
    return [0,1]

# 게임
def game(y,x,direction):
  global count
  global arr
  arr[y][x] = 1
  turn_count = 0
  
  while True:
    #1. turn left
    direction = turn_left(direction)
    #2. move_block
    dy, dx = move_block(direction)
    ry, rx = y+dy, x+dx
  
    # 3. 가보지 않은 칸이 존재
    if arr[ry][rx] == 0:
      count += 1
      arr[ry][rx] = 1
      y, x = ry, rx
      turn_count = 0
      continue
    else:
      turn_count += 1

      # 4 방향 전부 다 막혀있는 경우
      if turn_count == 4:
        dy, dx = move_block(direction)
        ry, rx = y-dy, x-dx

        # 4-1. 한 칸뒤로 갈 수 있는 경우
        if arr[ry][rx] == 0:
          y, x = ry, rx
        # 4-2. 갈수 없는 경우(종료)
        else:
          break
        turn_count = 0
        


n, m = map(int, input().split())
y, x, direction = map(int, input().split())
arr = []
for i in range(m):    
	arr.append(list(map(int, input().split())))
arr[y][x] = 1
count = 1
game(y,x,direction)
print(count)

