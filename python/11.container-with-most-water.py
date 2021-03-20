from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxArea = 0
        index = 0
        while left < right:
            minH = min(height[left], height[right])
            temp = (right - left) * minH
            if temp > maxArea:
                maxArea = temp
            if height[left] < height[right]:
                index = left + 1
                while height[index] < height[left] and left < right:
                    index += 1
                left = index
            else:
                index = right - 1
                while height[index] < height[right] and left < right:
                    index -= 1
                right = index
        return maxArea


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))