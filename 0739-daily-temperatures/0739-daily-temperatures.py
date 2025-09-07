class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []   # will store (temperature, index)

        for i in range(n):
            # check if today's temperature is warmer than the last one in stack
            while stack and temperatures[i] > stack[-1][0]:
                temp, idx = stack.pop()
                ans[idx] = i - idx
            stack.append((temperatures[i], i))
        
        return ans
        # stack = []
        # n = len(temperatures)
        # ans = [0] * n
        # for i in range(n):
        #     while stack and temperatures[i] > stack[-1][0]:
        #         temp, idx  =stack.pop()
        #         ans[idx] = i - idx
        #         stack.append((temperatures[i],i))

        # return ans 


        