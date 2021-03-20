class Solution:
    def numTrees(self, n: int) -> int:
        counter = [1] * (n + 1)
        for i in range(1, n+1):
            total = 0
            for j in range(1, i + 1):
                total += counter[i - j] * counter[j - 1]
            counter[i] = total
        return counter[n]


print(Solution().numTrees(4))