class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        # 내림차순 정렬
        nums.sort(reverse = True)
        pair = []
        sum_pair = 0
        
        for i in range(len(nums)):     
            pair.append(nums[i])
          
            if len(pair) == 2:
                sum_pair += min(pair)
                pair = []
            
        return sum_pair