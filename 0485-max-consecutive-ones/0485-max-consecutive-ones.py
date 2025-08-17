class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        count1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
            else:
                count = 0
            m = max(count,count1)
            count1 = m
        return count1
