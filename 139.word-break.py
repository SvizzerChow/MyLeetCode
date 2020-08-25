from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordMap = {}
        for word in wordDict:
            if word[0] not in wordMap:
                wordMap[word[0]] = []
            wordMap[word[0]].append(word)
        flags = [-1] * len(s)
        queue = [0]
        point = 0
        while point < len(queue):
            index = queue[point]
            if index >= len(s):
                break
            w = s[index]
            if w in wordMap:
                temp = wordMap[w]
                for wd in temp:
                    i = 1
                    while index + i < len(s) and i < len(wd):
                        if s[index+i] != wd[i]:
                            break
                        i += 1
                    if i == len(wd):
                        print(index, wd, i, index+i-1)
                        flags[index+i-1] = i
                        queue.append(index+i)
            point += 1
        print(flags)
        p = len(s) - 1
        while p >= 0:
            if flags[p] == -1:
                return False
            p -= flags[p]
        return True



s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(Solution().wordBreak(s, wordDict))
