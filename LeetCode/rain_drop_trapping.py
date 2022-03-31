# 정답 풀이: 투 포인터를 최대로 이동

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height : return 0
        
        l,r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        volume = 0
        
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max <= right_max:
                volume += left_max - height[l]
                l += 1
            else:
                volume += right_max - height[r]
                r -= 1
        
        return volume