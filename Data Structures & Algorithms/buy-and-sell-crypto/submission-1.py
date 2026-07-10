class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        final = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    final = max(prices[j] - prices[i] , final)

        return final
