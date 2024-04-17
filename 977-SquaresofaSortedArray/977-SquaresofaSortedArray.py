class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = [x * x for x in nums]
        new.sort()
        return new
        
[
