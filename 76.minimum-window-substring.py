
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        stack = []
        counter = {}
        for x in t:
            if counter.get(x) is None:
                counter[x] = [0, 0]
            counter[x][0] += 1
        addIndex = -1
        start = 0
        cutIndex = 0
        minStart = 0
        minEnd = len(s)
        keys = set(counter.keys())
        while addIndex < len(s) - 1:
            update = False
            for i in range(addIndex+1, len(s)):
                if s[i] in counter:
                    counter[s[i]][1] += 1
                    stack.append(i)
                    if counter[s[i]][0] <= counter[s[i]][1] and s[i] in keys:
                        keys.remove(s[i])
                    if len(keys) == 0:
                        addIndex = i
                        update = True
                        break
            if addIndex == -1:
                return ""
            for j in range(cutIndex, len(stack) - len(t)):
                if counter[s[stack[j]]][1] > counter[s[stack[j]]][0]:
                    cutIndex = j+1
                    start = stack[j+1]
                    counter[s[stack[j]]][1] -= 1
                else:
                    break
            if start < stack[cutIndex]:
                start = stack[cutIndex]
            if addIndex - start < minEnd - minStart:
                minEnd = addIndex
                minStart = start
            if not update:
                break
        return s[minStart:minEnd+1]


S = "aaaaaaaaaaaaaaaaaaaabaaac"
T = "acb"
print(Solution().minWindow(S, T))
