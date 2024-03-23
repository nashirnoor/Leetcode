        
            
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        val = set()
        for i in nums:
            if i in val:
                return i
            val.add(i)
        
[
