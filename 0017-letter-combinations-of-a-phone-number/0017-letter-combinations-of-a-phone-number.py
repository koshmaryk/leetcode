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

        output = []

        def gen(index, prefix):
            if len(prefix) == len(digits):
                output.append("".join(prefix))
                return

            for letter in digit_to_letters[digits[index]]:
                prefix.append(letter)
                gen(index + 1, prefix)
                prefix.pop()

        gen(0, [])
        return output
