class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        
        start = nums[0]
        
        for i in range(len(nums) - 1):
            if nums[i+1] != nums[i] + 1:
                end = nums[i]
                
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                
                start = nums[i+1]
        
       
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result
