total = 0
people= []
for i in range(4):
    outT, inT = map(int, input().split())
    total = total + inT - outT
    people.append(total)
print(max(people))