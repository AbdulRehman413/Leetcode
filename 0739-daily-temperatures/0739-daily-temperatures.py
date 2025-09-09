class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures 
        n = len(temps)
        ans = [0] * n
        stack = []
        for i , t in enumerate(temps):
            while stack and t > temps[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)

        return ans
      

        