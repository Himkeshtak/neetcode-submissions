class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #merge the arrays
        #sort the new array
        #if len of new arr odd
        #median is mid 
        #else mid + mid-1 /2
        new_array = nums1 + nums2
        new_array.sort()

        l,r = 0, len(new_array)-1
        median = 0

        mid = l + (r - l)//2

        if len(new_array)%2 == 0:
            median = float((new_array[mid] + new_array[mid+1])/2)
        else:
            median = new_array[mid]
        #while l<=r:
        #    mid = l + (r - l)//2
        #    if 
        return median