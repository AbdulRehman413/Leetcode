class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hashh = {}
        for i in s:
            hashh[i] = hashh.get(i,0) +1
        stack = []
        instack = set()
        for i , c in enumerate(s) :
            hashh[c] -=1

            if c in stack:
                continue

        
            while stack and stack[-1] > c and hashh[stack[-1]] > 0:
                removed = stack.pop()
                instack.remove(removed)

            stack.append(c)
            instack.add(c)

        return ''.join(stack)

            
        