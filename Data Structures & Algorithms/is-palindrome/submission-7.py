class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #s_no_space = s.replace(" ","")
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        n = len(cleaned)
        #*s = s_no_space[0]
        #*f = s_no_space[n]
        st = 0
        fi = n-1

        while st < fi:
            if(cleaned[st] != cleaned[fi]):
                return False
            
            st += 1
            fi -= 1
        return True