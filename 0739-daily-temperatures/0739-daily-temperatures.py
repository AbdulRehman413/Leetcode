class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                temp, idx  =stack.pop()
                ans[idx] = i - idx
            stack.append((temperatures[i],i))

        return ans 


        