class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #l, r = 0,0
        #
        #for i in range(len(nums)):
        #    if nums[i] == 1:
        #        l += 1
        #        r += 1
        #    elif nums[i] >= 1:
        
        # Two pointers wont work here
        #here we will use the greedy for in backward way (from the goal to the start of the array)
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

            
            