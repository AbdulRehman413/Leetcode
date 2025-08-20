class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        suma = sum(aliceSizes)
        sumb = sum(bobSizes)
        dif = (sumb - suma) /2
        bobset = set(bobSizes)

        for x in aliceSizes:
            y = x + dif
            if y in bobSizes:
                return [x,y]

        