from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = {}
        result = []
        for n in nums1:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
        for n2 in nums2:
            if n2 in counter and counter[n2] > 0:
                counter[n2] -= 1
                result.append(n2)
        return result


print(Solution().intersect([1,2,2,1], [2, 2]))
