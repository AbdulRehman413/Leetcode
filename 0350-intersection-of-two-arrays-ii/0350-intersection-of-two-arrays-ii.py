class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        for num in nums1:
            hash_map[num] = hash_map.get(num, 0) + 1  # build count map

        ans = []
        for num in nums2:
            if num in hash_map and hash_map[num] > 0:
                ans.append(num)           # keep duplicates
                hash_map[num] -= 1         # reduce count
                if hash_map[num] == 0:
                    del hash_map[num]      # remove if count hits zero

        return ans
