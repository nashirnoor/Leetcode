class Solution:
    def scoreOfString(self, s: str) -> int:
        arr = []
        for i in range(len(s)-1):
            if (ord(s[i])<=ord(s[i+1])):
              d = ord(s[i]) - ord(s[i+1])
            else:
              d = ord(s[i+1]) - ord(s[i])
            arr.append(d)
        return abs(sum(arr))
        
"
