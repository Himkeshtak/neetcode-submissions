class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        n = len(digits)
        num = 0
        for i in range(0,n):
            num += digits[i] * (10**(n-i-1))
        num += 1
        while(num > 0):
            res.append((num % 10))
            num = num//10
        
        res.reverse()
        return res




