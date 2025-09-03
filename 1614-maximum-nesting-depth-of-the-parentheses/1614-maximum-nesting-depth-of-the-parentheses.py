class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        maxco = 0
        stack = []
        for ch in  s:
            if ch == "(":
                counter +=1
                maxco= max(counter, maxco)
            elif ch == ")":
                counter  -=1 
               

        return maxco
        