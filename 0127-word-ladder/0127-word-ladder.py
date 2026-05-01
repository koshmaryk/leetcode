from collections import deque
from string import  ascii_lowercase

class Solution:
    '''
    
    hit -> [ait,bit,cit, ... zit, hat,hbt,hct,..hzt,...]

    cog
    
    TC O(N * M^2)
    SC O(N * M), where M is the length of the words and N is the number of words
    
    '''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        def get_neighbors(word):
            neighbors = []
            for i in range(len(word)):
                for letter in ascii_lowercase:
                    new_word = word[:i] + letter + word[i + 1:]
                    if new_word in words:
                        words.remove(new_word)
                        neighbors.append(new_word)
            return neighbors

        queue = deque([beginWord])
        levels = 0
        while queue:
            levels += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return levels

                for word in get_neighbors(curr):
                    queue.append(word)
        return 0