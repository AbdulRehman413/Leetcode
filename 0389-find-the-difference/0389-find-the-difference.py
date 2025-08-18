class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        hashh = {}
        hashh1 = {}
        if s is None:
            return t

        for i in s:
            hashh[i] = hashh.get(i,0) + 1
        for j in t:
            hashh1[j] = hashh1.get(j,0) + 1
        for k in hashh1:
            if k not in hashh or hashh1[k] > hashh.get(k, 0):
                return k
                        