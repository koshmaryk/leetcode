class TrieNode:
    def __init__(self,):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            for i, c in enumerate(word):
                if c == ".":
                    for child in node.children.values():
                        if dfs(child, word[i+1:]):
                            return True
                    return False
                elif c not in node.children:
                    return False
                else:
                    node = node.children[c]
            return node.is_word

        return dfs(self.root, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)