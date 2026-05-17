class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    # m - products length, n - searchWord length, L - longest product length
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        # m * L
        for product in products:
            curr = root
            for c in product:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True


        def dfs(node, prefix, suggestions):
            if len(suggestions) == 3:
                return
            if node.is_word:
                suggestions.append("".join(prefix))
            for c in sorted(node.children):
                prefix.append(c)
                dfs(node.children[c], prefix, suggestions)
                prefix.pop()

        
        output = []

        # n * L
        curr = root
        prefix = []
        for i, c in enumerate(searchWord):
            prefix.append(c)
            if curr:
                curr = curr.children.get(c)

            suggestions = []
            if curr:
                dfs(curr, prefix, suggestions)

            output.append(suggestions)
        return output