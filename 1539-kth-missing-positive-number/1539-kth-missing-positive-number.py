class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        i = 1
        j = 0
        
        while len(missing) < k:
            if j < len(arr) and arr[j] == i:
                j += 1
            else:
                missing.append(i)
            i += 1
        
        return missing[-1]
        