class Solution:
    def divisorGame(self, N: int) -> bool:
        flags = [[False, False] for _ in range(N+1)]
        if N == 1:
            return False
        for i in range(2, N+1):
            for j in range(i - 1, 0, -1):
                if i % j == 0:
                    temp = i - j
                    flags[i][0] = flags[i][0] or (flags[temp][1])
                    flags[i][1] = flags[i][1] or (flags[temp][0] or not flags[temp][1])
        print(flags)
        return flags[N][1]


print(Solution().divisorGame(4))