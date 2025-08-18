class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hashh = {}
        for i in magazine:
            hashh[i] = hashh.get(i,0) + 1
        for j in ransomNote:
            if j in hashh:
                hashh[j] -=1
            else:
                return False
            if hashh[j] < 0:
                return False
        return True