class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
                #impossible comnditions when no combination sis ther
            if i >= len(candidates) or total > target:
                return

            candidates[i]
            #1. cur.pop() (The Backtracking Step)
#Because Python lists are mutable objects passed by reference, all recursive calls share the exact same cur list in memory.
#
#What it does: It removes the candidate element you added in cur.append(candidates[i]) just before exploring that branch.
#
#Why it's needed: Once the DFS branch using candidates[i] finishes (either finding a valid sum or hitting an impossible condition), you must undo your change (backtrack). If you don't pop it, that element will remain stuck in cur and leak into completely unrelated decision branches, corrupting your combinations.
#
#2. dfs(i + 1, cur, total) (The "Skip" Decision)
#This algorithm makes a binary choice at each step:
#
#Include candidates[i]: Call dfs(i, ...) so you can reuse the element at index i.
#
#Exclude candidates[i]: Call dfs(i + 1, ...) to move on and try combinations using only the remaining candidates (from index i + 1 onward).
            #append the current candidate in the list
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res

             
