class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = []

        def backtrack(index, s):
            if len(s) == len(digits):
                combinations.append("".join(s))
                return

            letters = digit_to_letters[digits[index]]
            for letter in letters:
                s.append(letter)
                backtrack(index + 1, s)
                s.pop()

        backtrack(0, [])    
        return combinations

