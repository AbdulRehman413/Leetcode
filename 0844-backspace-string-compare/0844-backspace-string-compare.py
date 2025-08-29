class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
            stack = []
            stack2 = []
            for i in s:
                if i == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            stack= ''.join(stack)

            for i in t:
                if i == "#":
                    if stack2:
                        stack2.pop()
                else:
                    stack2.append(i)
            stack2 = ''.join(stack2)

            return stack == stack2
    

        # s = list(s)
        # i= 0
        # while i <len(s):
        #     if s[i] == "#":
        #         s.pop(i)
        #         if i > 0:

        #             s.pop(i-1)
        #             i-=1
        #     else:
        #         i+=1
        # s = ''.join(s)


        # t = list(t)
        # j = 0
        # while j < len(t):
        #     if t[j] == "#":
        #         t.pop(j)
        #         if j > 0:
                    
        #             t.pop(j-1)
        #             j-=1
        #     else:
        #         j+=1
        # t = ''.join(t)

        # return s == t
            

               
        