class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        dic1 = {}
        dic2 = {} 
        for i , j in zip(s,t):
            if i in dic1 and dic1[i] != j:
                return False

            if j in dic2 and dic2[j] != i:
                return False

            dic1[i] = j
            dic2[j] = i
        
        return True
            

           