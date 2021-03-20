class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) < len(s2):
            return False
        counter = {}
        tSet = set()
        for c in s2:
            tSet.add(c)
            if counter.get(c) is None:
                counter[c] = [0, 0]
            counter[c][0] += 1
        left = right = 0
        while right < len(s1):
            ch = s1[right]
            if ch in counter:
                counter[ch][1] += 1
                if counter[ch][0] == counter[ch][1]:
                    tSet.remove(ch)
            right += 1
            if len(tSet) == 0:
                while True:
                    temp = s1[left]
                    if temp in counter and counter[temp][0] == counter[temp][1]:
                        break
                    left += 1
                    if temp in counter:
                        counter[temp][1] -= 1
                if (right - left) == len(s2):
                    return True
        return False


s1 = "aaa"
s2 = "a"


print(Solution().checkInclusion(s1, s2))