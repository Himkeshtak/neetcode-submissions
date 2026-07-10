class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the min value(the pivot) an then make the two partiotion of the two arrayas and then use accordingly
        l , r = 0 , len(nums)-1

        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l 
        l , r = 0, len(nums) - 1

        if  target > nums[r]:
            r = pivot - 1
        else:
            l = pivot

        while l <= r:
            mid = l + (r - l)//2


            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1

