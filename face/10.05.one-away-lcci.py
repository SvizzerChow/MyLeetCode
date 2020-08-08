class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        lengthFirst = len(first)
        lengthSecond = len(second)
        if abs(lengthFirst - lengthSecond) > 1:
            return False
        if lengthFirst < 1 or lengthSecond < 1:
            return True
        start, end = 0, lengthFirst
        flag = True
        before, after = -1, lengthSecond - 1
        if start == end:
            if lengthSecond > lengthFirst:
                return first[0] == second[0] or first[0] == second[1]
            return True
        while start < end and start < lengthSecond and end > 0:
            if flag:
                if first[start] == second[start]:
                    before = start
                    start += 1
                else:
                    end -= 1
                    start -= 1
                    flag = False
            else:
                if first[end] == second[lengthSecond - lengthFirst + end]:
                    after = lengthSecond - lengthFirst + end
                    end -= 1
                else:
                    break
        return True if after - before + end - start <= 3 else False


first = "abc"
second = "bc"

print(Solution().oneEditAway(first, second))

