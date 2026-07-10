class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in {"+","-","*","/"}:
                stack.append(int(tokens[i]))
            elif tokens[i] == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
                a, b = 0,0
            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
                a, b = 0,0
            elif tokens[i] == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
                a, b = 0,0
            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
                a, b = 0,0

        return int(stack[0])