class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2] :
            return "0"

        n1, n2 = 0, 0
        
        # Fixed loop range and string-to-int conversion
        for i in range(len(num1)):
            n1 += (ord(num1[i]) - ord('0')) * (10 ** (len(num1) - i - 1))
            
        for i in range(len(num2)):
            n2 += (ord(num2[i]) - ord('0')) * (10 ** (len(num2) - i - 1))
            
        res = n1 * n2
        fin = []
        
        # Build digits list using integer division
        while res > 0:
            fin.append(str(res % 10))
            res //= 10
            
        return "".join(fin[::-1])