def recursion(words, l, r):
  global count 
  if l>=r : 
    return 1
  elif words[l] != words[r]: 
    return 0
  else: 
    count += 1
    return recursion(words, l+1, r-1)

def is_palindrome(words):
  return recursion(words, 0, len(words)-1)
  


num = int(input())
for _ in range(num):
  count = 1
  print(is_palindrome(input()), count)


