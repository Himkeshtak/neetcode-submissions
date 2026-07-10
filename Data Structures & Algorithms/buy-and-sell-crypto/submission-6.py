class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0  , 1
        final = 0
        while r < len(prices) :
            if prices[l] < prices[r]:
                final = max(prices[r]-prices[l], final)
            else:
                l = r
            r += 1

        return final