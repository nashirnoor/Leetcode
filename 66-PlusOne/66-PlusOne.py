class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
        str1 = ""
        d = 0
            str1 = str1+str(digits[i])
        d = int(str1) + 1
        
        res = [int(x) for x in str(d)]

        return res

[
