from heapq import heappush, heappop, nlargest
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
        h = nlargest(k, counter.items(), key=lambda x: x[1])
        result = []
        for x in h:
            result.append(x[0])
        return result

print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))