class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for num in s:
            dic1[num] = dic1.get(num, 0) +1
        for num in t:
            dic2[num] = dic2.get(num,0) + 1
        return dic1 == dic2