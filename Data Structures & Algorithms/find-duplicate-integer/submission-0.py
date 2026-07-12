class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #initialize a set and then keep all the values in the set
        # then if any element found which is already in the set then return that element , stop iteration

        unique = set()
        for i in range(len(nums)):
            if nums[i] in unique:
                rep_int = nums[i]
                return rep_int
            unique.add(nums[i])
            #curr = curr.next
        return rep_int
