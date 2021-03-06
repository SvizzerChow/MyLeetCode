from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start <= end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            if numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
        return []




print(Solution().twoSum([1,2,3,4,5,6,7,8], 10))
