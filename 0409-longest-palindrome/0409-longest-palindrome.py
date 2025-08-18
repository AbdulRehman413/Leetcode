class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashh = {}
        freq = []
        odd_found = False
        for i in s:
            hashh[i] = hashh.get(i,0) + 1
        for j in hashh:
            if hashh[j] %2 ==0:
                freq.append(hashh[j])
            else:
                freq.append(hashh[j]-1)
                odd_found = True
        if odd_found:
            return sum(freq) + 1
        else:
            return sum(freq)

            

            