class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashh = {}
        
        for i in  nums:
            hashh[i] = hashh.get(i,0) + 1
        maxlen = 0
        for x in hashh:
            if x+1 in hashh:
                length = hashh[x] + hashh[x+1]
                maxlen = max(maxlen,length)
        return maxlen

        