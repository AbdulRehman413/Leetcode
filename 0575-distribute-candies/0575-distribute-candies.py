class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # hashset = set(candyType)
        return min(len(set(candyType)), len(candyType)//2)
        # hashset = set()
        # for i in candyType:
        #     if i not in hashset:
        #         hashset.add(i)
        #     if len(set(hashset)) <= len(set(candyType)):
        #         return hashset
            


        