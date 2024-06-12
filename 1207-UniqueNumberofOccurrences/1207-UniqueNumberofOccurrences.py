class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        l1 = list(d.values())
        return len(l1) == len(l2)
        l2 = set(l1)
        
[
