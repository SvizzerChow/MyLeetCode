from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < 2:
            return [-1] * len(nums1)
        temp = [-1] * len(nums2)
        index = {nums2[-1]: len(nums2)-1}
        for i in range(len(nums2)-2, -1, -1):
            index[nums2[i]] = i
            t = i+1
            while t != -1:
                if nums2[t] > nums2[i]:
                    temp[i] = t
                    break
                t = temp[t]
        result = []
        for n in nums1:
            if temp[index[n]] > -1:
                result.append(nums2[temp[index[n]]])
            else:
                result.append(-1)
        return result


num1 = [137,59,92,122,52,131,79,236,94,171,141]
num2 = [137,59,92,122,52,131,79,236,94,171,141]

print(Solution().nextGreaterElement(num1, num2))

