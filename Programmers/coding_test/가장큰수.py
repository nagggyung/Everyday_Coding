def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = lambda x: x*3 ,reverse = True)
    
    # 모든 값이 0인경우를 처리하기 위해 int 로 변환한 뒤 str 로 변환해 준다. 
    return str(int(''.join(numbers)))