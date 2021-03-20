import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]
        i = len(matrix)
        while left < right:
            mid = (right + left)//2
            if self._check(matrix, i, mid, k):
                right = mid
            else:
                left = mid + 1
        return left


    def _check(self, matrix, n, mid, k):
        count = 0
        i = n - 1
        j = 0
        while 0 <= i and j < n:
            if matrix[i][j] <= mid:
                j += 1
                count += i + 1
            else:
                i -= 1
        return count >= k



print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))