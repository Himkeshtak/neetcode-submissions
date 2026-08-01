class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #iteration
        res = [[]]

        for num in nums:
            new_subsets = []
            #res += [subset + [num] for subset in res]

            for subset in res:
                new_subsets.append(subset + [num])

            res.extend(new_subsets)

        return res
