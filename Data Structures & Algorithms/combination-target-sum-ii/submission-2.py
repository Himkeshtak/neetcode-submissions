class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            
            # Decision 1:  Include candidate i
            cur.append(candidates[i])
            #use i+1 because each element can only be used once
            dfs(i + 1, cur, total + candidates[i])

            #Backtrack
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i + 1] :
                i += 1

            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res

            

            
            