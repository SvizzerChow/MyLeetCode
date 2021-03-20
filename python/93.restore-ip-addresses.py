from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)
        if length < 4 or length > 12:
            return []
        result = []
        flag = [[None, None, None] for _ in range(length)]
        self._getFlag(s, 0, length, flag, 1)
        print(flag)
        return self._getStr(s, 0, length, flag, 1)

    def _getFlag(self, s, i, length, flag, count):
        if count > 4 or i >= length:
            return
        for j in range(0, 3):
            t = flag[i][j]
            if t is None:
                t = self._check(s, i, j+1)
                flag[i][j] = t
            if t:
                self._getFlag(s, i + j + 1, length, flag, count + 1)

    def _check(self, s, start, length):
        temp = 0
        if s[start] == "0" and length > 1:
            return False
        for i in range(length):
            index = start + i
            if index >= len(s):
                break
            temp += (ord(s[start + i])-48)*10**(length-i-1)
        if temp > 255:
            return False
        return True

    def _getStr(self, s, i, length, flag, count):
        if count == 5 and i == length:
            return None
        elif i >= length or count > 4:
            return []
        result = []
        for j in range(0, 3):
            if flag[i][j]:
                rr = self._getStr(s, i+j+1, length, flag, count+1)
                if rr is None:
                    result.append(s[i:i + j + 1])
                elif len(rr) > 0:
                    for r in rr:
                        result.append(s[i:i+j+1]+"."+r)
        return result


print(Solution().restoreIpAddresses("010010"))