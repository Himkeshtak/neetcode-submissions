class Trienode:
    def __init__(self):
        self.children = {}
        self.endOfword = False

class WordDictionary:

    def __init__(self):
        self.root = Trienode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c]
        
        cur.endOfword = True      

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # try all possible child branches for the wildcard
                    for child in cur.children.values():
                        if dfs(i + 1,child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.endOfword
        return dfs(0, self.root)
