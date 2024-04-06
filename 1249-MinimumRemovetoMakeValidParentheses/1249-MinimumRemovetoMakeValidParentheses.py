                index = len(result) 
                stack.append(index)
            elif s[i] == ")":
                if len(stack) > 0 :
                    index = stack[-1]
                    stack.pop()
                    result = result[:index] + "(" + result[index:] + ")"
                else:
                    pass
            if s[i] == "(":
        for i in range(n):
        result = ""
        n = len(s)
        stack = []
    def minRemoveToMakeValid(self, s: str) -> str:
class Solution:
            else:
                result += s[i]
        
        return result
        
"
