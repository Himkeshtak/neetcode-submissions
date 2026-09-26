class Solution:
    def reverseBits(self, n: int) -> int:
        #parse the bits using the right shift and append in string 

        binary = ""
        for i in range(32):
            if (n>>i) & 1:
                binary += "1"
            else:
                binary += "0"
        print(binary)
        
        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= (1<< i)
        
        print(binary)
        return res
