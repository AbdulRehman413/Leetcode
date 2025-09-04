class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hashh = {}
        for i in range(len(nums)):
            if nums[i] in hashh:
                hashh[nums[i]] += 1
            else:
                hashh[nums[i]] =   1

        for i in hashh:
            if hashh[i] == 1:
                return i
        