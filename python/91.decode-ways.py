class Solution:
    def numDecodings(self, s: str) -> int:
        counter = [[-1, -1] for _ in range(len(s))]
        return self._dp(s, 0, counter)

    def _dp(self, s, start, counter):
        if counter[start][0] > -1:
            return counter[start][0] + counter[start][1]
        total = 0
        for i in [1, 2]:
            temp = self._canDecoding(s, start, i)
            count = 0
            if temp:
                if start + i == len(s):
                    count = 1
                elif counter[start+i][0] > -1:
                    count = counter[start+i][0] + counter[start+i][1]
                else:
                    count = self._dp(s, start+i, counter)
            counter[start][i-1] = count
            total += count
        return total

    def _canDecoding(self, s, start, length):
        if start + length > len(s):
            return False
        if s[start] == '0':
            return False
        num = 0
        for i in range(0, length):
            num = num * 10 + ord(s[start + i]) - 48
        return num <= 26


print(Solution().numDecodings("01"))