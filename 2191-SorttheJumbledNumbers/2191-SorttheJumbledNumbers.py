class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            ans = ""
            for char in str(num):
            res.append(int(ans))

        final = list(zip(nums, res))
                ans += str(mapping[int(char)])
        final = sorted(final, key=lambda x: x[1])
        return [tup[0] for tup in final]

[
[8,9,4,0,2,1,3,5,7,6]
[991,338,38]
[0,1,2,3,4,5,6,7,8,9]
[789,456,123]
[338,38,991]
[123,456,789]
[338,38,991]
[123,456,789]
