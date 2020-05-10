class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        start = 0
        end = 0
        sLength = len(s)
        for i in range(len(s)):
            j = 1
            while True:
                if i - j < 0 or i+j >= sLength:
                    j = j - 1
                    break
                if s[i-j] != s[i+j]:
                    j = j - 1
                    break
                else:
                    j = j+1

            j2 = 1
            while True:
                if i - j2 < -1 or i + j2 >= sLength:
                    j2 = j2 - 1
                    break
                if s[i - j2 + 1] != s[i + j2]:
                    j2 = j2 - 1
                    break
                else:
                    j2 = j2 + 1
            if j2* 2 > j* 2 + 1:
                if j2* 2 > maxLength:
                    maxLength = j2* 2
                    start = i - j2 + 1
                    end = i + j2
            else:
                if j* 2 + 1 > maxLength:
                    maxLength = j* 2 + 1
                    start = i - j
                    end = i + j 
        return s[start:end+1]

            
s = Solution()
print(s.longestPalindrome("abcbc"))