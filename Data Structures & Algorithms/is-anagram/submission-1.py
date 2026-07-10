class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #string1 = set()
        #string2 = set()
#
        #string1.add(s)
        #string2.add(t)        
        #if string1 == string2 :
        #    return True
#
        #return False
        
        # Second trial 

        #string1 = set()
        #string2 = set()
#
        #for i in range(len(s)):
        #   
        #    string1.add(s[i])
        #    string2.add(t[i])
        #
        #if string1 == string2:
        #   return True
        #return False
#
# third trial
        if sorted(s) == sorted(t):
            return True
        return False