from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        w1p = None
        w2p = None
        result = 1000000000
        for i in range(len(words)):
            if words[i] == word1:
                w1p = i
                if w2p is not None:
                    temp = w1p - w2p
                    if temp < result:
                        result = temp
            if words[i] == word2:
                w2p = i
                if w1p is not None:
                    temp = w2p - w1p
                    if temp < result:
                        result = temp
        return result