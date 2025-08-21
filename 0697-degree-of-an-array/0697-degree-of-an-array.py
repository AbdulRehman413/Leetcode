class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        hashh = {}
        first = {}
        last = {}
        for i , num in enumerate(nums):
            hashh[num] = hashh.get(num,0) + 1

            if num not in first:
                first[num] = i
                
            last[num] = i
        

        degree = max(hashh.values())

        min_length = len(nums)
        for num in hashh:
            if hashh[num] == degree:
                length = last[num] - first[num] + 1
                min_length = min(min_length, length)
        
        return min_length

            