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
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        n = len(folder)
        folder.sort()

        output = [folder[0]]
        for i in range(1, n):
            last_folder = output[-1]
            last_folder += "/"

            if not folder[i].startswith(last_folder):
                output.append(folder[i])
           
        return output