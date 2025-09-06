class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c:i for i,c in enumerate(s)} #last occurrence
        stack=[]
        seen= set()

        for i,c in enumerate(s):
            if c in seen:
                continue
            while stack and c < stack[-1] and i < last[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)
        # hashh = {}
        # for i in s:
        #     hashh[i] = hashh.get(i,0) +1
        # stack = []
        # instack = set()
        # for i , c in enumerate(s) :
        #     hashh[c] -=1

        #     if c in stack:
        #         continue

        
        #     while stack and stack[-1] > c and hashh[stack[-1]] > 0:
        #         removed = stack.pop()
        #         instack.remove(removed)

        #     stack.append(c)
        #     instack.add(c)

        # return ''.join(stack)

            
        