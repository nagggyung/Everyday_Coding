t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    sum = 0
    for j in range(len(nums)):
        if(j<11):
            sum+=nums[j]
    print(sum)