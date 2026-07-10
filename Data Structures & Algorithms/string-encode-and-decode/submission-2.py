class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_str = ""
        for i in range(len(strs)):
            #for j in range(len(strs[i])):
                encoded_str += strs[i]
                encoded_str += "~"
        return encoded_str


    def decode(self, s: str) -> List[str]:
         
        decoded_str = []
        current_word = ""
        
        for i in range(len(s)):

           if s[i] == "~":
               decoded_str.append(current_word)
               current_word = ""
               continue
           current_word += s[i]

        return decoded_str