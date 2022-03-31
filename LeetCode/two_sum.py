# 내 풀이
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        # 해시테이블 만들기 
        for i, num in enumerate(nums):
            hash[num] = i
        
        # two sum 확인
        for key in hash:
            if target-key in nums and hash[key] != nums.index(target-key):
                return [hash[key], nums.index(target-key)]