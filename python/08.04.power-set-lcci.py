from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 1:
            return []
        result = []
        for num in nums:
            for i in range(len(result)):
                result.append(result[i]+[num])
            result.append([num])
        result.append([])
        return result


print(Solution().subsets([1 , 2, 3]))

