class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0, k - 1
        res = []
        while r < len(nums):
            biggest = nums[l]
            for i in range(l,r+1):
                biggest = max(nums[i],biggest)
            res.append(biggest)
            l += 1
            r += 1
        return res