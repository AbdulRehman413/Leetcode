class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashh = {}
        # for i , num in enumerate(arr2):
        #     hashh[num] = i
        for i in arr1:
            hashh[i] = hashh.get(i,0) + 1

        

        

        result = []
        for n in arr2:
            if n in hashh:
                result.extend([n] * hashh[n])

        
        left = []
        for num in sorted(hashh):
            if num not in arr2:
                left.extend([num] * hashh[num])

        result.extend(left)
        

        return result

        
        

        
        