class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        map = {}
        for x in nums:
            for key in map:
                if x > key:
                    map[x].append(x)
                    