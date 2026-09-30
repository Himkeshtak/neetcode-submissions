class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        i, res = 0, 0 
        while(res != 1):
            res =0
            while(num > 0):
                res += (num % 10)**2
                num = num//10 
            if res == 1:
                return True
            if res in seen:
                return False
            num = res
            seen.add(res)
            i+= 1

