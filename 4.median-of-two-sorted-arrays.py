from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < 1 and len(nums2) < 1:
            return 0
        result = None
        even = (len(nums1) + len(nums2)) % 2 == 0
        mid = (len(nums1) + len(nums2)) // 2
        i = j = k = 0
        temp = None
        while True:
            if i == mid:
                result = self.getVal(nums1, nums2, j, k)
                if even:
                    result = (temp + result) / 2
                break
            i += 1
            if k == len(nums2) or (j < len(nums1) and nums1[j] < nums2[k]):
                temp = nums1[j]
                j += 1
            else:
                temp = nums2[k]
                k += 1
        return result

    def getVal(self, nums1: List[int], nums2: List[int], j, k):
        if j == len(nums1):
            return nums2[k]
        if k == len(nums2):
            return nums1[j]
        return min(nums1[j], nums2[k])


print(Solution().findMedianSortedArrays([1, 2], [4, 5]))
