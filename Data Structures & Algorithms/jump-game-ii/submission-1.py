class Solution:
    def jump(self, nums: List[int]) -> int:
        #goal = len(nums) - 1

        #for i in range(len(nums) -2,-1,-1):
        #    #agar koi number ka value bada hai ki goal ke paar jayega uska jump to chalega, its ok
        #    if i + nums[i] >= goal:
        #        goal = i

        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0 
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res