class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tsum = 0
        id_sum = 0
        for i in range(0,len(nums)):
            tsum += nums[i]
        for j in range(0,len(nums)+1):
            id_sum += j 
        if tsum != id_sum:
            return id_sum - tsum
        else:
            return 0
            