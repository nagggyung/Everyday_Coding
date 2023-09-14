class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        for i in range(len(nums)-1):
            if not res:
                res.append(1)
            
            p *= nums[i]
            res.append(p)
        
        p = 1
        for j in range(-1,-(len(nums)+1), -1):
            res[j] *= p
            p *= nums[j]
        
        return res