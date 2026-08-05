class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # If popped item is forming a valid parnetheses then continue recursively calling it everytime , I am thinking to solve this question with the stack and then recuresively creating the sjubset for it
        stack = []
        res = []
        
        #if stack[i] == ")" and stack 
        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(stack))
                return

            # Step-1 here we add the open parentheses if we have remaining open ones
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()  # Backtrack step

            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop() # bactrack step

        backtrack(0,0)
        return res