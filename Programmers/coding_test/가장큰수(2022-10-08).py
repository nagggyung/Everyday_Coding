# 의외로 풀이를 생각해 내기 어려웠던 문제이다.. 
# x*3 을 하여 3개의 숫자 씩 비교하기위한 아이디어를 
# 생각하지 못하여 해맸었던거 같다. 


def solution(numbers):
    temp_list = []
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int("".join(numbers)))

'''
1. x*3 해주는 이유?
각 num이 1000이하 이므로
lambda x : x*3은 num 인자 각각의 문자열을 3번 반복한다는 뜻이다. x*3을 하는 이유? -> num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.
2. int 했다가 str 하는 이유?
모든 값이 0일 때(즉, '000'을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다. 

'''