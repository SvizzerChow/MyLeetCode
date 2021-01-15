from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        counter = {}
        pSet = set()
        for c in p:
            pSet.add(c)
            if c not in counter:
                counter[c] = [0, 0]
            counter[c][0] += 1
        left = right = 0
        while right < len(s):
            ch = s[right]
            if ch in counter:
                counter[ch][1] += 1
                if counter[ch][0] == counter[ch][1]:
                    pSet.remove(ch)
            right += 1
            if len(pSet) == 0:
                while True:
                    if (len(result) == 0 or result[-1] != left) and (right - left) == len(p):
                        result.append(left)
                    cleft = s[left]
                    if cleft in counter and counter[cleft][0] == counter[cleft][1]:
                        break
                    left += 1
                    if cleft in counter:
                        counter[cleft][1] -= 1
        return result

