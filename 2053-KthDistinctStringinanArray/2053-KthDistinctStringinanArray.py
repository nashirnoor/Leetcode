class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in arr:
            if dic[i]==1:
                k-=1
                if k==0:
                    return i
        return ""
        
[
["d","b","c","b","c","a"]
2
["aaa","aa","a"]
1
["a","b","a"]
3
"a"
"aaa"
""
"a"
"aaa"
""
