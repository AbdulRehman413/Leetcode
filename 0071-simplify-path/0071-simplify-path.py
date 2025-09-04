class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        for ch in parts:
            if ch == "" or ch == ".":
                continue
            elif ch == "..":
                if stack:  
                    stack.pop()
            else:
                stack.append(ch)

        return "/" + "/".join(stack)
        #     if ch in ["", "."]:
        #         continue
        #     elif ch == "..":
        #         if stack and stack[-1] != "/":
        #             stack.pop()
        #         if stack and stack[-1] == "/":
        #             stack.pop()

            
        #     else:
        #         if not stack or stack[-1] != "/":
        #             stack.append("/")
        #         stack.append(ch)

        # if not stack:
        #     return "/"

        # return ''.join(stack)

        

        
        
        