class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr = 0
        
       
        for i in range(k):
            curr += nums[i]
        
        maxavg = curr / k

        for i in range(k, n):
            curr += nums[i]       
            curr -= nums[i - k]   
            avg = curr / k
            maxavg = max(maxavg, avg)
        
        return maxavg