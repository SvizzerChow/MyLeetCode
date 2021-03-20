class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        counterMap = {}
        for i in range(len(s)):
            if s[i] not in counterMap:
                counterMap[s[i]] = 0
            counterMap[s[i]] += 1
        for cc in counterMap.keys():
            if counterMap.get(cc) < k:
                return max(self.longestSubstring(temp, k) for temp in s.split(cc))
        return len(s)


print(Solution().longestSubstring("baaabcb", 3))

