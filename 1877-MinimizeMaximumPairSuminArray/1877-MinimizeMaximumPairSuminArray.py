class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        l = len(nums)
        for i in range(l // 2):
            pair_sum = nums[i] + nums[l - 1 - i]  
            max_sum = max(max_sum, pair_sum)  
        return max_sum
        nums.sort()
        
[
