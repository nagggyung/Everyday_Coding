def find_loc(loc):
  arr = list(loc)
  x = x_list.index(arr[0])
  y = int(arr[1])
  return [y,x]

direction_map = [
  [1, -2],
  [-1, -2],
  [1, 2],
  [-1, 2],
  [2, -1],
  [-2, -1],
  [2, 1],
  [-2, 1]
]
x_list = ['-9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y, x = find_loc(input())

count = 0

for i in range(len(direction_map)):
  dy, dx = direction_map[i]
  ry, rx = y+dy, x+dx
  if ry < 1 or ry > 8 or rx < 1 or rx > 8:
    continue
  count += 1

print(count)


