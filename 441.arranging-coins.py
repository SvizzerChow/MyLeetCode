class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = -0.5 + 0.5 * (1 + 8*n)**0.5
        return int(x)

print(Solution().arrangeCoins(8))