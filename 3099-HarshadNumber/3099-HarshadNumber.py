class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        fin = 0
        for i in str(x):
            fin += int(i)
        return fin if x % fin == 0 else -1
        
1
