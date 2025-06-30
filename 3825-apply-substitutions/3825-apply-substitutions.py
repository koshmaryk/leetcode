class Solution:
    # A, B -> C 
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        hashmap = {k:v for k,v in replacements}
        while "%" in text:
            for k,v in hashmap.items():
                text = text.replace(f"%{k}%", v)
        return text
        