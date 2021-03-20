class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count = 0
        x = [0]*len(s1)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                x[count] = i
                count += 1
        if count % 2 == 1:
            return -1
        total = 0
        diff = 0
        for j in range(0, count, 2):
            if s1[x[j]] == s1[x[j + 1]]:
                total += 1
            else:
                diff += 1
        if diff > 0:
            total += diff // 2 * 2 + diff % 2 * 2
        return total


s1 = "xxyyxyxyxx"
s2 = "xyyxyxxxyx"
print(Solution().minimumSwap(s1, s2))
