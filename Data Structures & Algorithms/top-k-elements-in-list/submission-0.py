class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}
        #unique = set()
        freq = List[List[int]]

        for i in range(len(nums)):
            seen[nums[i]] = 1 + seen.get(nums[i], 0)

        arr = []
        for num, count in seen.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
           
                

