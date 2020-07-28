import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        index = {}
        for n in nums:
            s = str(n)
            if s[0] not in index:
                index[s[0]] = []
            index[s[0]].append(s)
        result = ''
        if len(index) == 1 and '0' in index:
            return '0'
        for i in range(9, -1, -1):
            s = str(i)
            if s not in index:
                continue
            for item in sorted(index[s], reverse=True, key=functools.cmp_to_key(cmp)):
                result += item
        return result


def cmp(a, b):
    i = j = 0
    while i < len(a) or j < len(b):
        if i == len(a):
            i = 0
        elif j == len(b):
            j = 0
        if a[i] > b[j]:
            return 1
        elif a[i] < b[j]:
            return -1
        if i < len(a):
            i += 1
        if j < len(b):
            j += 1
    if len(a) == len(b):
        return 0
    return 1 if len(a) < len(b) else -1


print(Solution().largestNumber([121, 12]))
