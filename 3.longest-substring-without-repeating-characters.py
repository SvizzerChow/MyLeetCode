class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result = 0
        left = right = 0
        counter = {}
        while right < len(s):
            ch = s[right]
            if ch in counter and counter[ch] >= left:
                left = counter[ch]
                result = max(result, right - left)
                left += 1
            else:
                result = max(result, right - left + 1)
            counter[ch] = right
            right += 1
        return result


print(Solution().lengthOfLongestSubstring("abcaa"))
