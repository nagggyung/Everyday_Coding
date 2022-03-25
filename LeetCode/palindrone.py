class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 빈 문자열 선언
        res_str = ""

        # 한 문자씩 소문자로 변환하여 문자열에 넣기
        for c in s:
            if c.isalnum():
                res_str += c.lower()

        reversed_str = res_str[::-1]
        return res_str == reversed_str
    