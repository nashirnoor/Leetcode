class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums)+1):
            count = 0
            for elem in nums:
                if elem >= x:
                    count+=1
            if count == x:
                return x
        return -1
        
[3,5]
