class Trienode:
    def __init__(self):
        self.children = {}
        self.endOfword = False
class PrefixTree:

    def __init__(self):

        self.root = Trienode()

    def insert(self, word: str) -> None:
        """inserts a word into the trie"""
        cur = self.root # start at the root node
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trienode()
            cur = cur.children[c]
        cur.endOfword = True

    def search(self, word: str) -> bool:
        """returns if the word is in the trie"""
        cur = self.root

        for c in word: #Go character by character in the word
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfword

    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix"""
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        