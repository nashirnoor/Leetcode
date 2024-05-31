class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in nums:
            if nums.count(i)==1:
                arr.append(i)
        return arr
        
[1,2,1,3,2,5]
