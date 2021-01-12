from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < 1 and len(nums2) < 1:
            return 0
        mid = (len(nums1) + len(nums2)) // 2
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.getKValue(nums1, nums2, mid+1)
        else:
            return (self.getKValue(nums1, nums2, mid) + self.getKValue(nums1, nums2, mid+1)) / 2

    def getKValue(self, nums1: List[int], nums2: List[int], k):
        index1 = index2 = 0
        length1 = len(nums1)
        length2 = len(nums2)
        while k > 1:
            if length1 < 1:
                return nums2[index2 + k-1]
            if length2 < 1:
                return nums1[index1 + k-1]
            if index1 >= length1 or index2 >= length2:
                break
            half = k//2
            temp1 = min(index1 + half, length1) - 1
            temp2 = min(index2 + half, length2) - 1
            if nums1[temp1] <= nums2[temp2]:
                k -= (temp1 - index1) + 1
                index1 = temp1 + 1
            else:
                k -= (temp2 - index2) + 1
                index2 = temp2 + 1
        if index1 >= length1:
            return nums2[index2 + k-1]
        if index2 >= length2:
            return nums1[index1 + k-1]
        return min(nums1[min(index1, length1-1)], nums2[min(index2, length2-1)])


print(Solution().findMedianSortedArrays([1], [2,3,4,5,6]))

