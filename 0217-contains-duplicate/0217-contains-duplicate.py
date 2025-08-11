class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = 0
        for r in range(1, len(nums)):
            if nums[l] == nums[r]:
                return True 
        return False
     
