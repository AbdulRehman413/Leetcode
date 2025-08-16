class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = list(enumerate(nums))
        indexed_nums.sort(key=lambda x: x[1])  # sort by values

        l, r = 0, len(indexed_nums) - 1
        while l < r:
            s = indexed_nums[l][1] + indexed_nums[r][1]
            if s == target:
                return indexed_nums[l][0], indexed_nums[r][0]  # return original indices
            elif s < target:
                l += 1
            else:
                r -= 1
