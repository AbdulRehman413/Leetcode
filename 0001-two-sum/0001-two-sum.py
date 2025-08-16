class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in dic:
                return [dic[dif] ,i]
            dic[num] = i
        