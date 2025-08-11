class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = []
        l = 0
        for r in range(1, len(nums)):
            if nums[l] == nums[r]:
                dic.append(nums[l])
        
        # Remove duplicates
        new_dic = set(dic)

        # If you still want it as an integer
        final_number = int(''.join(map(str, sorted(new_dic))))
        return final_number
