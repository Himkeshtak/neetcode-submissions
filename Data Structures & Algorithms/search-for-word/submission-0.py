class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        # to comapre and serach each and every neighbour of the current letter of the word
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (min(r, c) < 0 or
                r >= ROWS or c  >= COLS or # grid ke nbaahr ke elemnets naa dekhe
                word[i] != board[r][c] or  # the letter not ,mathced
                (r, c) in path):           # already seen
                return False

            path.add((r, c))  # Flaggin the letter already visisted
            res = (dfs(r + 1, c, i+1) or
                   dfs(r - 1, c, i+1) or
                   dfs(r, c + 1, i+1) or
                   dfs(r, c - 1, i+1)) 
            
            path.remove((r, c))
            return res

        # this to iterate over each and every element of the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False