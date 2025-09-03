class Solution:
    def maxDepth(self, s: str) -> int:
       
        stack = []
        maxco = 0
        for ch in  s:
            if ch == "(":
                stack.append(ch)
                maxco= max(len(stack), maxco)
            elif ch == ")":
                stack.pop()
               

        return maxco
        