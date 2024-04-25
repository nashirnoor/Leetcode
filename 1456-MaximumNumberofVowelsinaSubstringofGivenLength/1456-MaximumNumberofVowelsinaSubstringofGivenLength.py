        currCount: int = 0
        vowels: str = "aeiou"            
        for i, v in enumerate(s):
            if i >= k:
                if s[i-k] in vowels:
                    currCount -= 1
            if s[i] in vowels:
                

        ans: int = 0            
    def maxVowels(self, s: str, k: int) -> int:
class Solution:
                currCount += 1
            ans = max(currCount, ans)
        return ans
        
"
