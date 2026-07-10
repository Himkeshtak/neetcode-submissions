class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_strs = [None] * len(strs)
        internal = []
        
        visited = [False] * len(strs)

        for i in range(len(strs)):
            sorted_strs[i] = sorted(strs[i])
        
        for i in range(len(strs)):

            if visited[i]:
                continue

            internal.append([])

            internal[-1].append(strs[i])
            visited[i] = True

            for j in range(i+1, len(strs)):
                if sorted_strs[i] == sorted_strs[j] : 
                    internal[-1].append(strs[j])
                    visited[j] = True

        return internal
           

