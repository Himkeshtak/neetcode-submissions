class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [None]*len(nums)
        
        for i in range(len(nums)):
            current_element = 1
            for j in range(len(nums)):
                if i!=j:
                    current_element *= nums[j]
            output[i] = current_element    

        return output
            
