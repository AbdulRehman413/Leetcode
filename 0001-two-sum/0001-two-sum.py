class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l<r:
            s = nums[l] + nums[r]
            if s == target:
                return l,r
            elif s < target:
                l+=1
            else:
                r-=1
        