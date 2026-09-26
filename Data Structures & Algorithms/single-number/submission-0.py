class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use hashmaps for the all the integers
        count_map = {}

        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        for num, count in count_map.items():
            if count == 1:
                return num
            # if value of the key integer is 1 then return key
