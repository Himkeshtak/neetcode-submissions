class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return False

        stack = []
        stackvalue = ""
        outvalue = ""
        for i in range(len(s)):
            

            if s[i] in ["(", "{","["]:
                stack.append(s[i])
                continue

            elif s[i] in [")", "]", "}"] :
                
                if not stack:
                    return False
                
                stackvalue = stack.pop()
                outvalue = s[i]
            
            if not (
               (stackvalue == "(" and outvalue == ")") or
               (stackvalue == "{" and outvalue == "}") or
               (stackvalue == "[" and outvalue == "]") ) :   
                return False
        
        return len(stack) == 0
