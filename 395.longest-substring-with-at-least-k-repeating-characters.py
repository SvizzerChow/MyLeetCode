class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counterMap = {}
        for i in range(len(s)):
            if s[i] not in counterMap:
                counterMap[s[i]] = []
            counterMap[s[i]].append(i)
        noChar = set()
        for cc in counterMap.keys():
            if len(counterMap.get(cc)) < k:
                noChar.add(cc)
        if len(noChar) <= 0:
            return len(s)
        if len(noChar) == len(s):
            return 0
        start = index = 0
        end = 1
        length = len(s)
        maxLength = 0
        having = set()
        while index < length:
            if s[index] in noChar:
                start = index = start + 1
                end = start + 1
                having = set()
                continue
            if s[index] not in having:
                temp = self._getIndex(index, counterMap[s[index]], k)
                if temp == -1:
                    start = index = start + 1
                    end = start + 1
                    having = set()
                    continue
                if end < temp:
                    end = temp
                having.add(s[index])
            if index == end:
                l = end - start + 1
                if l > maxLength and l >= k:
                    print(start, end, s[start:end + 1])
                    maxLength = l
                end += 1
            index += 1
        return maxLength

    def _getIndex(self, i, temp, k):
        p = 0
        for jj in range(len(temp)):
            if temp[jj] == i:
                p = jj
                break
        if p + k - 1 < len(temp):
            return temp[p + k - 1]
        return -1



print(Solution().longestSubstring("baaabcb", 3))

