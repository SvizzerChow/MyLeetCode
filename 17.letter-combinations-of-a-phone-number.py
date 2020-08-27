from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is None or digits == '':
            return []
        numMap = {}
        for i in range(2, 10):
            numMap[str(i)] = self._getStrs(i)
        print(numMap)
        return self._merge(digits, 0, numMap)

    def _merge(self, s, index, numMap):
        now = numMap[s[index]]
        if index == len(s)-1:
            return now
        after = self._merge(s, index+1, numMap)
        result = []
        for i in range(len(now)):
            temp = now[i]
            for ss in after:
                result.append(temp + ss)
        return result

    def _getStrs(self, n):
        k = 3
        if n == 7 or n == 9:
            k = 4
        temp = 0 if n < 8 else 1
        result = []
        for i in range(k):
            result.append(chr(97+(n-2)*3+i+temp))
        return result


print(Solution().letterCombinations("23"))