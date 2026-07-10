class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        print(len(numbers))
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    if numbers[i] != numbers[j]:
                        return [i+1,j+1]
            #index1 += index1
            #index2 += index2
                    