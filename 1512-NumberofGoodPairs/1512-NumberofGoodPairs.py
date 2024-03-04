class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = {}
        res = 0
        for number in nums:            
            if number in h:
                res += h[number]
                h[number] += 1
            else:
                h[number] = 1
        return res
        
[
