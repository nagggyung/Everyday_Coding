def factorial(num):
  if num == 0:
    return 0
  if num == 1:
    return 1

  return factorial(num-1) + factorial(num-2)


num = int(input())
print(factorial(num))

