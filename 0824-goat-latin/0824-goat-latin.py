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
        words = sentence.split(" ")
        for idx, word in enumerate(words):
            if word[0].lower() in vowel:
                s = word
            else:
                s = word[1:] + word[0]
            
            s = s + "ma" + "a" * cnt
            words[idx] = s

            cnt += 1

        return " ".join(words)
    