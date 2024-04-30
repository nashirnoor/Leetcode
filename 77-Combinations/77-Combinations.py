        res = []
        comb = []
        backtract(1)
        return res
        def backtract(start):
            if len(comb)==k:
                res.append(comb[:])
                return
            
            for num in range(start, n+1):
                comb.append(num)
                backtract(num+1)
                comb.pop()
         
    def combine(self, n: int, k: int) -> List[List[int]]:
class Solution:
4
