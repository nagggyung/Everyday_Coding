num = int(input())
words = []

for _ in range(num):
  word = input()
  if word not in words:
    words.append(word)

# 길이먼저, 길이가 같은 경우에는 사전 순 정렬
words.sort(key=lambda x: (len(x),x))

for word in words:
  print(word)