from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = 0
        counter = [0] * len(nums)
        result = [0, 0]
        for n in nums:
            counter[n-1] += 1
            if counter[n - 1] > 1:
                result[0] = n
            else:
                total += n
        result[1] = (1 + len(nums))*len(nums) >> 2 - total
        return result


print(Solution().findErrorNums([1, 2, 2, 3, 5]))