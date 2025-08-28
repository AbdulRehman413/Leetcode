class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # s = list(s)
   
        # stack = []
        # stack.append(s)
        # for i in range(len(s)):
        #     if i == "#":
        #         stack.pop()
        #     else:
        #         return 1
        s = list(s)
        i= 0
        while i <len(s):
            if s[i] == "#":
                s.pop(i)
                if i > 0:

                    s.pop(i-1)
                    i-=1
            else:
                i+=1
        s = ''.join(s)


        t = list(t)
        j = 0
        while j < len(t):
            if t[j] == "#":
                t.pop(j)
                if j > 0:
                    
                    t.pop(j-1)
                    j-=1
            else:
                j+=1
        t = ''.join(t)

        return s == t
            

               
        