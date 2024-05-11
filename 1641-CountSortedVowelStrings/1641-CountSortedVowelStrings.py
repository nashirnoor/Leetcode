class Solution:
    def countVowelStrings(self, n: int) -> int:
        d4,d3,d2,d1 = 5,10,10,5
        for i in range(1,n):
            d4+=d3
            d3+=d2
            d2+=d1
            d1+=1
        return d4
        
1
