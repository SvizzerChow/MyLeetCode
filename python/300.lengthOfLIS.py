from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        maxLength = 1
        counter = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j] and counter[j] + 1 > counter[i]:
                    counter[i] = counter[j] + 1
            if counter[i] > maxLength:
                maxLength = counter[i]
        print(counter)
        return maxLength


print(Solution().lengthOfLIS([10,9,2,5,3,4]))