        lo = 0
        hi = len(people)-1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
        people.sort()
    def numRescueBoats(self, people: List[int], limit: int) -> int:
class Solution:
[
