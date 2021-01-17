from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        counter = [[0, 0] for _ in range(len(nums))]
        counter[0][1] = nums[0]
        for i in range(1, len(nums)-1):
            counter[i][0] = max(counter[i-1][0], counter[i-1][1])
            counter[i][1] = counter[i-1][0] + nums[i]
        result = max(counter[-2][0], counter[-2][1])
        counter = [[0, 0] for _ in range(len(nums))]
        counter[1][1] = nums[1]
        for i in range(2, len(nums)):
            counter[i][0] = max(counter[i-1][0], counter[i-1][1])
            counter[i][1] = counter[i-1][0] + nums[i]
        return max(result, counter[-1][0], counter[-1][1])


print(Solution().rob([200,3,140,20,10]))