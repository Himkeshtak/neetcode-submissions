class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
            
        consecutive_count = 1
        max_count = 1
        #new_nums = sorted(nums)
        uniques = sorted(list(set(nums)))
        #uniques = new_nums
        for i in range(1,len(uniques)):
            if uniques[i] == uniques[i-1] + 1 :
                #if consecutive_count == 0:
                #    consecutive_count += 1
                
                
                consecutive_count += 1 
            else:
                consecutive_count = 1
            #if nums[i] == nums[i-1]:
            #if nums
            #elif len(uniques) == 1:
            #    consecutive_count += 1
            if consecutive_count > max_count:
                max_count = consecutive_count

        return max_count