class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using the Kadane bhai ka algo , jisme agar sum is less than zero 
        # to element shift karke karo
        maxsub , cursum = nums[0], 0
        for num in nums:
            if cursum < 0:
                cursum = 0
            cursum += num
            maxsub = max(maxsub, cursum)
        return maxsub 