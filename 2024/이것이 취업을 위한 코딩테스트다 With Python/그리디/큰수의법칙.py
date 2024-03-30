# N: 배열의 크기
# M: 숫자가 더해지는 횟수
# K:  제한 횟수

# 풀이 방식 1
def question1(m: int, k: int, arr: list):
    arr.sort(reverse=True)

    num1 = arr[0]
    num2 = arr[1]

    count = 1
    result = 0

    for i in range(m):
        if count > k:
            result += num2
            count = 1

            continue

        result += num1
        count += 1

    print(result)

# 풀이 방식 2
# 가장 큰수와 두번 째로 큰수가 몇번 씩 더해지는지 규칙을 찾아서 연산

def question2(m: int, k: int, arr: list):
    arr.sort(reverse= True)
    first = arr[0]
    second = arr[1]

    first_count = (m // k) * k
    second_count = m % k
    
    result = first*first_count + second*second_count
    
    print(result)




n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
question1(m, k, arr)
question2(m, k, arr)

