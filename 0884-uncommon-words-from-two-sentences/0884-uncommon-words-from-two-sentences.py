class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = list(set(s1.split()))
        s2 = list(set(s2.split()))
        if len(s1) and len(s2) <=2:

            if s1 not in s2:
                return s2
            if s2 not in s1:
                return s1
        
        for i , j in zip(s1,s2):
            if i!=j:
                return i,j

        
