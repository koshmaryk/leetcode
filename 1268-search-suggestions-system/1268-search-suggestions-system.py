class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        root = TrieNode()
        for product in products:
            curr = root
            for c in product:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_end = True

        output = []

        def dfs(node, prefix, suggestions):
            if len(suggestions) == 3:
                return
            if node.is_end:
                suggestions.append(prefix)
            for c in sorted(node.children):
                dfs(node.children[c], prefix + c, suggestions)


        curr = root
        for i, c in enumerate(searchWord):
            if curr:
                curr = curr.children.get(c)
                
            suggestions = []
            if curr:
                dfs(curr, searchWord[:i+1], suggestions)

            output.append(suggestions)
        return output
        