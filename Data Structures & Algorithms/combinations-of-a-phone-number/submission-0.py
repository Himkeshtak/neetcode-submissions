class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        curr = []
        res = []
        if digits == "":
            return res
        key_2 = ("a","b","c")
        key_3 = ("d","e","f")
        key_4 = ("g","h","i")
        key_5 = ("j","k","l")
        key_6 = ("m","n","o")
        key_7 = ("p","q","r","s")
        key_8 = ("t","u","v")
        key_9 = ("w","x","y","z")

        keys = {
            "2": key_2, "3": key_3, "4":key_4,
            "5": key_5, "6": key_6, "7": key_7,
            "8": key_8, "9": key_9
        }
        def dfs(i):
            if i >= len(digits):
                res.append("".join(curr))
                return
            for char in keys[digits[i]]:
                curr.append(char)
                dfs(i + 1)
                curr.pop()

        #pass starting from the index 0
        dfs(0)
        return res