class Solution:
    def reorderLogFiles(self, logs) -> List[str]:

        str_list = []
        int_list = []

        # 문자 vs 숫자로 구분
        for log in logs:
           if log.split()[1].isalpha():
               str_list.append(log)
           else:
               int_list.append(log)

        # str_list 정렬
        str_list.sort(key = lambda x : (x.split()[1:],x.split()[0]))

        return str_list + int_list
