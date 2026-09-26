class Solution:
    def hammingWeight(self, n: int) -> int:
        count  = 0
        for i in range(32):
            # this performs AND operations between the right most bit and the 1
            if (n>>i) & 1: 
                count += 1
        return count