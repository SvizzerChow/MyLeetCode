from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self._getStrs(digits)



    def _getStrs(self, s):
        k = 3
        if s == '9':
            k=4
        n = ord(s) - 49
        result = []
        for i in range(k):
            result.append(chr(97+(n-1)*3+i))
        return result


print(Solution().letterCombinations("2"))