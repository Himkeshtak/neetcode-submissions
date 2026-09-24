class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        nextdp = [False] * (target + 1)

        dp[0] = True
        for i in range(len(nums)):
            for j in range(1, target + 1):
                if j >= nums[i]:
                    nextdp[j] = dp[j] or dp[j - nums[i]]
                else:
                    nextdp[j] = dp[j]
            dp, nextdp = nextdp, dp

        return dp[target]