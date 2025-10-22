class Solution(object):
    def groupAnagrams(self, strs):
        hashh = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in hashh:
                hashh[key].append(i)
            else:
                hashh[key] = [i]

        return list(hashh.values())
        