class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # sys.maxsize => int의 최댓 값 
        min_value = sys.maxsize
        max_price = 0
        
        for price in prices:
            min_value = min(min_value, price)
            max_price = max(price - min_value, max_price)
        
        return max_price