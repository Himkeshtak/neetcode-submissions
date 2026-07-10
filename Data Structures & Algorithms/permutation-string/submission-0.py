class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {} # keep all the permutation of the s1 string in the hashmap
        
        for char in s1:
            s1_count[char] = 1 + s1_count.get(char, 0)

        l = 0
        r = len(s1) - 1
        for i in range(len(s2)):
            
            #this makes static slinding window
            l = i
            r = i + len(s1) - 1

            #fetch the substring from l->r
            substring = s2[l : r + 1]

            #count the characters in the current l->r window
            sub_count = {}
            for char in substring:
                sub_count[char] = 1 + sub_count.get(char,0)

            if sub_count == s1_count:
                return True

        return False 




        # store the s1 chars in hashmaps
        # if the chars from l->r matches the chars in the hashtable return true
        # else return false


        # this problem is of the static sliding window