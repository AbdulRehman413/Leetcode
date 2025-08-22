class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        hashh =  {}
        for i in words[0]:
            hashh[i] = hashh.get(i,0) + 1
        

        for j in words[1:]:
            curr = {}
            for ch in j:
                curr[ch] = curr.get(ch,0) + 1

            for ch in list(hashh.keys()):
                if ch in curr:
                    hashh[ch] = min(hashh[ch] , curr[ch])
                else:
                    del hashh[ch]

        result = []
        for ch, count in hashh.items():
            result.extend([ch]*count)

        return result 

        