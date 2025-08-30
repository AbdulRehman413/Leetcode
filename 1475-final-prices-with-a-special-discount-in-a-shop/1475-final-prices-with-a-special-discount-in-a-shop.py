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
        n = len(prices)
        result = []
        
        for i in range(n):
            discount = 0
            # look for the first smaller-or-equal price to the right
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            result.append(prices[i] - discount)
        
        return result