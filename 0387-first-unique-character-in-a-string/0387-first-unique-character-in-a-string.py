class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashh = {}
        for i in s:
            hashh[i] = hashh.get(i, 0) + 1
        for j , num in enumerate(s):
            if hashh[num] == 1:
                return j
        return -1
