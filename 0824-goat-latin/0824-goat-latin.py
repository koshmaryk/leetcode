class Solution:
    '''
    I speak Goat Latin

    I
    speak
    Goat
    Latin

    '''
    def toGoatLatin(self, sentence: str) -> str:
        vowel = set(['a', 'e', 'i', 'o', 'u'])

        cnt = 1
        words = sentence.split(" ") # O(N)
        for idx, word in enumerate(words): # O(N)
            if word[0].lower() in vowel: # O(1)
                s = word
            else:
                s = word[1:] + word[0] # O(w) slice + O(w) concat
            
            s = s + "ma" + "a" * cnt # O(w + cnt) concat, O(cnt) repeat 
            words[idx] = s

            # cnt grows 1,2,3...k → sum = k(k+1)/2 = O(k²)
            # k = number of words, so total added chars are O(k²) → O(n²)

            cnt += 1

        return " ".join(words) # O(total length of all words)
        # O(n²), n + (1+2+...+k) = n + O(k²) = O(n²)
    