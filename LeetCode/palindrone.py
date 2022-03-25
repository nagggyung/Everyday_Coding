from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # deque 선언
        deq = deque()

        # 한 문자씩 소문자로 변환하여 큐에 넣기
        for c in s:
            if c.isalnum():
                deq.append(c.lower())

        reversed_deq = reversed(deq)
        return list(deq) == list(reversed_deq)