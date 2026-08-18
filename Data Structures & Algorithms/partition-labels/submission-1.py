class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # can be done using the sliding window concept
        # Use the hashmaps to track that the number of times it is present in the array
        unique = {}
        res = []

        #just append the string in the hashmap we built
        for char in s:
            unique[char] = unique.get(char, 0) + 1
        
        window = {}
        size = 0
        
        for i in range(len(s)):
            char = s[i]
            size += 1

            window[char] = window.get(char, 0)
            unique[char] -= 1

            if unique[char] == 0:
                del unique[char]
                del window[char]
            
            if len(window) == 0:
                res.append(size)
                size = 0
                
        return res

        # loop through the string with marking each element as visited and reducing from the hashmap and adding them in the empty list , as soon as the all the unique elements of the substring values in hashmap append them in the resulting list
   
            