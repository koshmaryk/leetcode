"""
a
  b
c d
  d e
  f

a 
  b  c
     d


"/a","/a/b","/c/d","/c/d/e","/c/f"

a/b
a/ba


"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        n = len(folder)

        root = TrieNode()
        for f in folder:
            curr = root
            fnames = f.split("/")[1:]
            for fname in fnames:
                if fname not in curr.children:
                    curr.children[fname] = TrieNode()
                curr = curr.children[fname]
            curr.is_end = True

        output = []
        for f in folder:
            curr = root
            fnames = f.split("/")[1:]

            subfolder = False
            for i, fname in enumerate(fnames):
                curr = curr.children[fname]
                if curr.is_end and i != len(fnames) - 1:
                    subfolder = True
                    break
            
            if not subfolder:
                output.append(f)
       
        return output