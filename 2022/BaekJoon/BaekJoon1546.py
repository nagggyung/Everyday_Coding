n = int(input())
scores = list(map(int, input().split()))
maxScore = max(scores)
newScores = []
for i in range(len(scores)):
    a = scores[i]/maxScore*100
    newScores.append(a)
print(sum(newScores)/n)