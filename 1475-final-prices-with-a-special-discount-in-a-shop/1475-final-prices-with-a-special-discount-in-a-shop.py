class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # stack = []
        # n = len(prices)

        # for i in range(n-1,-1,-1):
        #     while stack and stack[-1] > prices[i]:
        #         stack.pop()
        #     if stack:
        #         prices[i] -= stack[-1]
        #     stack.append(prices[i])


        # return prices 
        stack = []
        for i, a in enumerate(prices):
            while stack and prices[stack[-1]] >= a:
                prices[stack.pop()] -= a
            stack.append(i)
        return prices