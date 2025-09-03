class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        for i , c in enumerate(word):
            if ch not in word:
                return word
            if c == ch:
              
                stack.append(ch)
                stack = stack[::-1]
                return ''.join(stack) + word[i+1:]
                

                
            else:
                stack.append(c)

        return ''.join(stack)
       
       
        


        