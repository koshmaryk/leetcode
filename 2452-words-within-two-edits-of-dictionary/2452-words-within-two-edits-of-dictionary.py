"""
l -> o OR r


wolss

w
  o
    o
      d
        a
    r
      s
        s  


"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        root = TrieNode()
        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_end = True


        def dfs(query, i, node, cnt):
            if cnt > 2:
                return False

            if i == len(query):
                return True

            next_node = node.children.get(query[i])
            if next_node and dfs(query, i + 1, next_node, cnt):
                return True

            if cnt < 2:
                for number in range(26):
                    c = chr(ord('a') + number)
                    next_node = node.children.get(c)
                    if query[i] != c and next_node and dfs(query, i + 1, next_node, cnt + 1):
                        return True
            return False
                
        output = []
        for query in queries:
            curr = root
            if dfs(query, 0, curr, 0):
                output.append(query)
        return output
