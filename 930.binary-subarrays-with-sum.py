from typing import List


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        index = []
        length = len(A)
        for i in range(length):
            if A[i] == 1:
                index.append(i)
        if len(index) < S:
            return 0
        total = 0
        left = 0
        beforeIndex = -1
        if S == 0:
            if len(index) == 0:
                return (length+1)*length//2
            else:
                for j in index:
                    if j > left:
                        total += (j - left+1) * (j - left)//2
                    left = j + 1
                if index[-1] < length - 1:
                    temp = length - 1 - index[-1]
                    total += (temp + 1) * temp // 2
            return total
        for j in range(S - 1, len(index)):
            indexJ = index[j]
            before = index[left] - beforeIndex
            after = index[j+1] - indexJ if j+1 < len(index) else length - indexJ
            total += before*after
            beforeIndex = index[left]
            left += 1
        return total

print(Solution().numSubarraysWithSum([0,1,1,1,1], 3))