class Solution:
    def isPalindrome(self, s: str) -> bool:
        res1 = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                res1 = "".join([res1, i])
        res1 =res1.lower()
        d = res1[::-1]
        if d == res1:
            return True
        return False
        


        
"
