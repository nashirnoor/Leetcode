            if item[0] not in ret:
                ret[item[0]] = item[1]
            else:
                ret[item[0]] += item[1]
        for item in new:
        new.extend(items2)
        new.extend(items1)
        new = []
        ret = {}
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
class Solution:
[
