from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) >> 1
            if arr[left] == target:
                return left
            if arr[left] < target:
                if arr[mid] > target:
                    right = mid
                else:
                    left += 1
            else:
                if arr[mid] > arr[left]:
                    left = mid + 1
                else:
                    left += 1
        if left < len(arr) and arr[left] == target:
            return left
        return -1


print(Solution().search([12, 20, -21, -21, -19, -14, -11, -8, -8, -8, -6, -6, -4, -4, 0, 1, 5, 5, 6, 11, 11, 12], -8))