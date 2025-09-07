class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashh = {}
        for num in arr:
            hashh[num] = hashh.get(num, 0) + 1
        
        # Step 2: Check uniqueness
        seen = set()
        for count in hashh.values():
            if count in seen:
                return False
            seen.add(count)
        
        return True
        