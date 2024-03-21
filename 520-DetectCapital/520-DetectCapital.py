class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower():
            return True
        else:
            return False
        elif word == word.capitalize():
            return True
        
"
