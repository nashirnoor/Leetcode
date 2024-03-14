    def isIsomorphic(self, s: str, t: str) -> bool:
class Solution:
        new = dict()
        for i in range(len(s)):
                if t[i] in new.values():
                    return False
                new[s[i]] = t[i]
            elif new[s[i]]!=t[i]:
                return False
        return True

                

        
            if s[i] not in new.keys():

"
