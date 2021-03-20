from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        m = {self.getR(nums[0], k) : 0}
        s = nums[0]
        for i in range(1, len(nums)):
            s += nums[i]
            r = self.getR(s, k)
            if r == 0:
                return True
            x = m.get(r)
            if x is not None:
                if i - x > 1:
                    return True
            else:
                m[r] = i
        return False

    def getR(self, n, k):
        if k == 0:
            return n-0
        return n % k


print(Solution().checkSubarraySum([0, 0, 1], 0))

