def solution(phone_book):
    
    # phone_book 리스트 정렬 -> 다른 번호의 접두어인 경우 숫자가 붙어있다.
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    
    return True