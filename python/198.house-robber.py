from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        counter = [[0, 0] for _ in range(len(nums))]
        counter[0][1] = nums[0]
        for i in range(1, len(nums)):
            counter[i][0] = max(counter[i-1][0], counter[i-1][1])
            counter[i][1] = counter[i-1][0] + nums[i]
        return max(counter[-1][0], counter[-1][1])