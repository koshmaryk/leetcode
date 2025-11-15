class Solution:
    '''
    
    hit -> [ait,bit,cit, ... zit, hat,hbt,hct,..hzt,...]

    cog
    
    
    '''
    from collections import deque
    from string import ascii_lowercase

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def neighbors(word):
            neighbors = []
            for i, c in enumerate(word):
                for letter in ascii_lowercase:
                    new_word = word[:i] + letter + word[i+1:]
                    if new_word in words:
                        words.remove(new_word)
                        neighbors.append(new_word)
            return neighbors


        words = set(wordList)
        queue = deque([beginWord])
        levels = 0
        while queue:
            size = len(queue)
            levels += 1
            for i in range(size):
                curr = queue.popleft()
                if curr == endWord:
                    return levels
                for word in neighbors(curr):
                    queue.append(word)
        return 0