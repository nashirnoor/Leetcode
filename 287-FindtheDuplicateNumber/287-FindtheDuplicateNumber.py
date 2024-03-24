class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        val = set()
        for i in nums:
            if i in val:
                return i
            val.add(i)
            
        
        
[1,3,4,2,2]
